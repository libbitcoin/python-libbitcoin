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

    def __init__(self, make_future=zmq.asyncio.Future,
                       make_zmq_poller=zmq.asyncio.Poller,
                       make_zmq_context=zmq.asyncio.Context):
        self._make_future = make_future
        self._make_zmq_poller = make_zmq_poller
        self._make_zmq_context = make_zmq_context

        zmq_poller = make_zmq_poller()
        self._poller = libbitcoin.server.poller.Poller(zmq_poller)

        self.zmq_context = make_zmq_context()

        self._scheduler = libbitcoin.server.scheduler.Scheduler()

    def Client(self, address, settings=ClientSettings()):
        return libbitcoin.server.client.Client(address, self, settings)

    def Future(self):
        return self._make_future()

    @property
    def poller(self):
        return self._poller
    @property
    def scheduler(self):
        return self._scheduler

    # asyncio prefers them called.
    def tasks(self):
        return [
            self.poller.run(),
            self.scheduler.run()
        ]

    def stop_all(self):
        self.poller.stop()
        self.scheduler.stop()

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

    @property
    def loop(self):
        return IOLoop.current()

