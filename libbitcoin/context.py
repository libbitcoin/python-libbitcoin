import zmq.asyncio
import libbitcoin.client
import libbitcoin.poller
import libbitcoin.scheduler

try:
    # TornadoContext
    import tornado.concurrent
except:
    pass

import zmq.eventloop.future

class Context:

    def __init__(self, make_future=zmq.asyncio.Future,
                       make_zmq_poller=zmq.asyncio.Poller,
                       make_zmq_context=zmq.asyncio.Context):
        self._make_future = make_future
        #self._make_zmq_poller = make_poller
        #self._make_zmq_context = make_context

        zmq_poller = make_zmq_poller()
        self._poller = libbitcoin.poller.Poller(zmq_poller)

        self.zmq_context = make_zmq_context()

        self._scheduler = libbitcoin.scheduler.Scheduler()

    def Client(self, address):
        return libbitcoin.client.Client(address, self)

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
        super().__init__(
            make_future=tornado.concurrent.Future,
            make_zmq_poller=zmq.eventloop.future.Poller,
            make_zmq_context=zmq.eventloop.future.Context
        )

    # Tornado prefers them uncalled.
    def start(self, loop):
        loop.spawn_callback(self.poller.run)
        loop.spawn_callback(self.scheduler.run)

