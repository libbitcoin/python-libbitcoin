import asyncio
import libbitcoin.binary
import libbitcoin.bitcoin_utils

class SubscribeResult:

    def __init__(self, address_version, address_hash,
                 height, block_hash, tx_data):
        self.address = libbitcoin.bitcoin_utils.hash_160_to_bc_address(\
            address_version, address_hash)
        self.confirmed = height > 0
        self.height = height
        self.block_hash = block_hash
        self.tx_data = tx_data
        self.prefix_blocks = address_hash

class Subscription:

    def __init__(self, prefix, data, client):
        self._prefix = prefix
        self._data = data
        self._client = client
        self._queue = asyncio.Queue()
        self._stopped = False
        self._reschedule()

    async def _renew(self):
        if not self.is_running():
            return
        # Does the server send a reply?
        ec = await self._client._renew(self._data)
        if ec:
            print("Warning: client didn't renew subscription.", ec,
                  file=sys.stderr)
            return
        self._reschedule()

    def _reschedule(self):
        scheduler = self._client._context.scheduler
        renew_time = self._client.settings.renew_time
        scheduler.add(renew_time, self._renew)

    async def updates(self):
        update = await self._queue.get()
        if type(update) == StopIteration:
            raise update
        return update

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return True

    def is_running(self):
        return not self._stopped

    async def stop(self):
        self._stopped = True
        await self._queue.put(StopIteration())

    def _match(self, address_hash):
        matcher = libbitcoin.binary.Binary(self._prefix.size, address_hash)
        return matcher == self._prefix

    async def handle_update(self, result):
        if not self._match(result.prefix_blocks):
            return
        await self._queue.put(result)

class SubscribeManager:

    def __init__(self):
        self._subscriptions = []

    def add(self, subscription):
        self._subscriptions.append(subscription)

    async def update(self, result):
        for sub in self._subscriptions:
            await sub.handle_update(result)

    def clean_expired(self):
        self._subscriptions = [sub for sub in self._subscriptions
                               if not sub.is_running()]

