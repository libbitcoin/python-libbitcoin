import asyncio
import zmq.asyncio
import libbitcoin.server.client
import libbitcoin.server.poller
import libbitcoin.server.scheduler
from libbitcoin.server import ClientSettings

try:
    # Used by TornadoContext
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import AsyncIOMainLoop
except:
    pass

import zmq.eventloop.future

class Context:

    def __init__(self):
        self.zmq_context = zmq.asyncio.Context()
        self._clients = []

    def Client(self, address, settings=ClientSettings()):
        client = libbitcoin.server.client.Client(self, address, settings)
        self._clients.append(client)
        return client

    def stop(self):
        [client.stop() for client in self._clients]

class TornadoContext(Context):

    def __init__(self):
        # Tell asyncio to use zmq's eventloop
        zmq.asyncio.install()
        # Tell tornado to use asyncio
        AsyncIOMainLoop().install()
        super().__init__(
            make_future=zmq.asyncio.Future,
            make_zmq_poller=zmq.asyncio.Poller,
            make_zmq_context=zmq.asyncio.Context
        )

    def spawn(self, callback, *args, **kwargs):
        return IOLoop.current().spawn_callback(callback, *args, **kwargs)

    # Tornado prefers them uncalled.
    def start(self):
        loop = IOLoop.current()
        loop.spawn_callback(self.poller.run)
        loop.spawn_callback(self.scheduler.run)
        loop.start()

    def stop(self):
        loop = IOLoop.current()
        self.spawn(loop.stop)

    @property
    def loop(self):
        return IOLoop.current()

