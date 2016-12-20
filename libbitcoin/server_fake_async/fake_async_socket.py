import asyncio
import struct
import sys
import threading
import zmq

class FrameHandler:

    def __init__(self, context):
        context.register(self)
        self._futures = {}
        self._handlers = {}

    async def stop(self):
        [future.cancel() for future in self._futures.values()]

    async def receive(self, frame):
        reply = self._deserialize(frame)
        if reply is None:
            print("Error: bad reply sent by server. Discarding.",
                  file=sys.stderr)
            return
        command, reply_id, *_ = reply
        if reply_id in self._futures:
            # Lookup the future based on request ID
            future = self._futures[reply_id]
            del self._futures[reply_id]
            # Set the result for the future
            try:
                future.set_result(reply)
            except asyncio.InvalidStateError:
                # Future timed out.
                pass
        elif command in self._handlers:
            handler = self._handlers[command]
            await handler(frame)
        else:
            print("Error: unhandled frame %s:%s." % (command, reply_id))

    def _deserialize(self, frame):
        if len(frame) != 3:
            return None
        return [
            frame[0],                               # Command
            struct.unpack("<I", frame[1])[0],       # Request ID
            struct.unpack("<I", frame[2][:4])[0],   # Error Code
            frame[2][4:]                            # Data
        ]

    def add_future(self, request_id, future):
        self._futures[request_id] = future

    def delete_future(self, request_id):
        del self._futures[request_id]

    def add_handler(self, command, handler):
        self._handlers[command] = handler

class ThreadsafeFakeAsyncSocket(threading.Thread):

    def __init__(self, context, url, settings):
        super().__init__()
        self._poller = zmq.Poller()
        self._schedule = context.spawn
        self._frame_handler = FrameHandler(context)
        context.register(self)

        self._response_queue = asyncio.Queue()
        self._stopped = False
        self._timeout = 0.1

        self._context = zmq.Context()
        self._server_socket = self._context.socket(zmq.DEALER)
        if settings.socks5:
            socks5 = bytes(settings.socks5, "ascii")
            self._server_socket.setsockopt(zmq.SOCKS_PROXY, socks5)
        self._server_socket.connect(url)

        self._consumer_socket = self._context.socket(zmq.PULL)
        self._consumer_socket.bind("inproc://send-queue")

        self._producer_socket = self._context.socket(zmq.PUSH)
        self._producer_socket.connect("inproc://send-queue")

        self._register(self._server_socket)
        self._register(self._consumer_socket)

        self.start()
        self._schedule(self._process_loop)

        self._stop_future = asyncio.Future()

    def add_future(self, request_id, future):
        self._frame_handler.add_future(request_id, future)

    def delete_future(self, request_id):
        self._frame_handler.delete_future(request_id)

    def add_handler(self, command, handler):
        self._frame_handler.add_handler(command, handler)

    def _register(self, socket):
        self._poller.register(socket, zmq.POLLIN)

    async def stop(self):
        self._stopped = True
        self.join()
        await self._stop_future

    def run(self):
        while not self._stopped:
            # Allow timeouts in case new sockets are added
            # when poller started.
            events = self._poller.poll(timeout=0.1)
            for socket, mask in events:
                self._process(socket)

    def _process(self, socket):
        if socket == self._consumer_socket:
            request = socket.recv_multipart()
            self._server_socket.send_multipart(request)
        elif socket == self._server_socket:
            self._receive(socket)

    def _receive(self, socket):
        response = socket.recv_multipart()
        self._schedule(self._response_queue.put, response)

    async def _process_loop(self):
        while not self._stopped:
            try:
                frame = await asyncio.wait_for(self._response_queue.get(),
                                                  self._timeout)
            except asyncio.TimeoutError:
                continue
            await self._frame_handler.receive(frame)
            self._response_queue.task_done()
        self._stop_future.set_result(True)

    def send(self, request):
        self._producer_socket.send_multipart(request)

