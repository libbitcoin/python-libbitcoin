from tornado.ioloop import IOLoop
from tornado.platform.asyncio import AsyncIOMainLoop

class TornadoContext:

    def __init__(self):
        # Tell tornado to use asyncio
        AsyncIOMainLoop().install()
        self._objects = []

    def spawn(self, callback, *args, **kwargs):
        return self.loop.spawn_callback(callback, *args, **kwargs)

    def call_later(self, callback, *args):
        return self.loop.call_later(callback, *args)

    def register(self, obj):
        self._objects.append(obj)

    # Tornado prefers them uncalled.
    def start(self):
        self.loop.start()

    def stop(self):
        self.spawn(self._stop_all)

    async def _stop_all(self):
        for obj in self._objects:
            await obj.stop()
        self.spawn(self.loop.stop)

    @property
    def loop(self):
        return IOLoop.current()

