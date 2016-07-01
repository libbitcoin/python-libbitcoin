import struct
import sys
import zmq

class Poller:

    def __init__(self, zmq_poller):
        self._zmq_poller = zmq_poller
        self._futures = {}
        self._handlers = {}
        self._stopped = False

    async def run(self):
        while not self._stopped:
            # Allow timeouts in case new sockets are added
            # when poller started.
            events = await self._zmq_poller.poll(timeout=0.1)
            for socket, mask in events:
                await self._receive(socket)

    async def _receive(self, socket):
        # Get the reply
        frame = await socket.recv_multipart()
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
            future.set_result(reply)
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

    def register(self, socket):
        self._zmq_poller.register(socket, zmq.POLLIN)

    def add_future(self, request_id, future):
        self._futures[request_id] = future

    def add_handler(self, command, handler):
        self._handlers[command] = handler

    def stop(self):
        self._stopped = True

