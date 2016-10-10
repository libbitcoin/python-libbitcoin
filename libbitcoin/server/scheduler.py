import asyncio
import time

class Scheduler:

    def __init__(self):
        self._items = []
        self._time = time.time()
        self._stopped = False

    def add(self, remaining_seconds, func):
        self._items.append([remaining_seconds, func])

    async def update(self):
        time_now = time.time()
        ticks = time_now - self._time
        self._time = time_now
        for item in self._items:
            item[0] -= ticks
            time_remaining, func = item
            if time_remaining < 0:
                self._items.remove(item)
                await func()

    async def run(self):
        while self.is_running():
            await self.update()
            await asyncio.sleep(1)

    def is_running(self):
        return not self._stopped

    def stop(self):
        self._stopped = True

