import random
import struct
import enum
import asyncio
import sys
import zmq
import libbitcoin.server
import libbitcoin.server.serialize
import libbitcoin.server.bitcoin_utils
import libbitcoin.server.subscribe

def create_random_id():
    MAX_UINT32 = 4294967295
    return random.randint(0, MAX_UINT32)

def make_error_code(ec):
    if not ec:
        return None
    return libbitcoin.server.ErrorCode(ec)

def pack_block_index(index):
    if type(index) == bytes:
        assert len(index) == 32
        return libbitcoin.server.serialize.serialize_hash(index)
    elif type(index) == int:
        return struct.pack('<I', index)
    else:
        raise ValueError("Unknown index type")

def unpack_table(row_fmt, data):
    # get the number of rows
    row_size = struct.calcsize(row_fmt)
    nrows = len(data) // row_size

    # unpack
    rows = []
    for idx in range(nrows):
        offset = idx * row_size
        row = struct.unpack_from(row_fmt, data, offset)
        rows.append(row)
    return rows

class PointIdent(enum.Enum):
    output = 0
    spend = 1

class ClientSettings:

    def __init__(self):
        self._renew_time = 5 * 60
        self._query_expire_time = None
        self._socks5 = None

    @property
    def renew_time(self):
        """The renew time for address or stealth subscriptions.
        This number should be lower than the setting for the blockchain
        server. A good value is server_renew_time / 2"""
        return self._renew_time
    @renew_time.setter
    def renew_time(self, renew_time):
        self._renew_time = renew_time

    @property
    def query_expire_time(self):
        """The timeout for a query in seconds. If this time expires
        then the blockchain method will return libbitcoin.server.ErrorCode
        Set to None for no timeout."""
        return self._query_expire_time
    @query_expire_time.setter
    def query_expire_time(self, query_expire_time):
        self._query_expire_time = query_expire_time

    @property
    def socks5(self):
        """Enable SOCKS5."""
        return self._socks5
    @socks5.setter
    def socks5(self, socks5):
        self._socks5 = socks5

class Poller:

    def __init__(self, socket):
        self._socket = socket
        self._futures = {}

        loop = asyncio.get_event_loop()
        self._task = loop.create_task(self._run())

    async def _run(self):
        while True:
            await self._receive()

    def stop(self):
        self._task.cancel()

    async def _receive(self):
        # Get the reply
        frame = await self._socket.recv_multipart()
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

class Client:

    def __init__(self, context, url, settings=ClientSettings()):
        self._url = url
        self.settings = settings
        self._setup_socket(context)

        self._poller = Poller(self._socket)
        #self._subscribe_manager = libbitcoin.server.subscribe.SubscribeManager()

    def stop(self):
        self._poller.stop()

    def _setup_socket(self, context):
        self._socket = context.zmq_context.socket(zmq.DEALER)
        if self.settings.socks5:
            socks5 = bytes(self.settings.socks5, "ascii")
            self._socket.setsockopt(zmq.SOCKS_PROXY, socks5)
        self._socket.connect(self._url)
        #self._context.poller.register(self._socket)
        #self._context.poller.add_handler(b"address.update", self._on_update)

    async def _send_request(self, command, request_id, data):
        request = [
            command,
            struct.pack("<I", request_id),
            data
        ]
        await self._socket.send_multipart(request)

    async def request(self, request_command, request_data):
        """Make a generic request. Both options are byte objects specified like
        b"blockchain.fetch_block_header" as an example."""
        future = asyncio.Future()
        request_id = create_random_id()
        self._poller.add_future(request_id, future)

        await self._send_request(request_command, request_id, request_data)

        expiry_time = self.settings.query_expire_time
        try:
            reply = await asyncio.wait_for(future, expiry_time)
        except asyncio.TimeoutError:
            self._poller.delete_future(request_id)
            return libbitcoin.server.ErrorCode.channel_timeout, None

        reply_command, reply_id, ec, data = reply
        assert reply_command == request_command
        assert reply_id == request_id
        ec = make_error_code(ec)
        return ec, data

    async def block_header(self, index):
        """Fetches the block header by height or integer index."""
        command = b"blockchain.fetch_block_header"
        data = pack_block_index(index)
        ec, data = await self.request(command, data)
        if ec:
            return ec, None
        return ec, data

    async def history(self, address, from_height=0):
        """Fetches history for an address. Returns an error code,
        and a list of rows consisting of outputs and corresponding
        spend inputs.

        Outputs are a tuple of:

            OutPoint(hash, index)
            block height
            value

        Spends are either None (if unspent) or:

            InPoint(hash, index)
            block height

        These values form a tuple for each row in the history."""

        command = b"address.fetch_history2"

        address_version, address_hash = \
            libbitcoin.server.bitcoin_utils.bc_address_to_hash_160(address)

        # prepare parameters
        data = struct.pack('B', address_version)    # address version
        data += address_hash                        # address
        data += struct.pack('<I', from_height)      # from_height

        ec, data = await self.request(command, data)
        if ec:
            return ec, None

        outputs = []
        spends = {}
        # parse results
        rows = unpack_table("<B32sIIQ", data)
        for id, hash, index, height, value in rows:
            id = PointIdent(id)
            if id == PointIdent.output:
                point = libbitcoin.server.models.OutPoint()
            elif id == PointIdent.spend:
                point = libbitcoin.server.models.InPoint()
            point.hash = hash[::-1]
            point.index = index
            if id == PointIdent.output:
                outputs.append((point, height, value))
            elif id == PointIdent.spend:
                spends[value] = (point, height)

        history = []
        for output in outputs:
            output_point, *_ = output
            checksum = output_point.checksum()
            try:
                row = (output, spends[checksum])
            except KeyError:
                row = (output, None)
            history.append(row)

        return ec, history

    async def last_height(self):
        """Fetches the height of the last block in our blockchain."""
        command = b"blockchain.fetch_last_height"
        ec, data = await self.request(command, b"")
        if ec:
            return ec, None
        # Deserialize data
        height = struct.unpack("<I", data)[0]
        return ec, height

    async def transaction(self, tx_hash):
        """Fetches a transaction by hash from the blockchain."""
        command = b"blockchain.fetch_transaction"
        data = libbitcoin.server.serialize.serialize_hash(tx_hash)
        ec, data = await self.request(command, data)
        if ec:
            return ec, None
        return ec, data

    async def transaction_from_pool(self, tx_hash):
        """Fetches a transaction by hash from the transaction pool."""
        command = b"transaction_pool.fetch_transaction"
        data = libbitcoin.server.serialize.serialize_hash(tx_hash)
        ec, data = await self.request(command, data)
        if ec:
            return ec, None
        return ec, data

    async def spend(self, outpoint):
        """Fetches a corresponding spend of an output."""
        command = b"blockchain.fetch_spend"
        data = outpoint.serialize()
        ec, data = await self.request(command, data)
        if ec:
            return ec, None
        spend = libbitcoin.server.models.InPoint.deserialize(data)
        return ec, spend

    async def transaction_index(self, tx_hash):
        """Fetch the block height that contains a transaction and its index
        within that block."""
        command = b"blockchain.fetch_transaction_index"
        data = libbitcoin.server.serialize.serialize_hash(tx_hash)
        ec, data = await self.request(command, data)
        if ec:
            return ec, None, None
        height, index = struct.unpack("<II", data)
        return ec, height, index

    async def block_transaction_hashes(self, block_hash):
        """Fetches list of transaction hashes in a block by block hash."""
        command = b"blockchain.fetch_block_transaction_hashes"
        data = libbitcoin.server.serialize.serialize_hash(block_hash)
        ec, data = await self.request(command, data)
        if ec:
            return ec, None
        rows = unpack_table("32s", data)
        hashes = [row[0][::-1] for row in rows]
        return ec, hashes

    async def block_height(self, block_hash):
        """Fetches the height of a block given its hash."""
        command = b"blockchain.fetch_block_height"
        data = libbitcoin.server.serialize.serialize_hash(block_hash)
        ec, data = await self.request(command, data)
        if ec:
            return ec, None
        height = struct.unpack("<I", data)[0]
        return ec, height

    async def stealth(self, prefix, from_height=0):
        """Fetch possible stealth results. These results can then be iterated
        to discover new payments belonging to a particular stealth address.
        This is for recipient privacy.

        The prefix is a special value that can be adjusted to provide
        greater precision at the expense of deniability.

        from_height is not guaranteed to only return results from that
        height, and may also include results from earlier blocks.
        It is provided as an optimisation. All results at and after
        from_height are guaranteed to be returned however."""
        command = b"blockchain.fetch_stealth"
        data = struct.pack('<B', prefix.size)
        data += prefix.blocks
        data += struct.pack('<I', from_height)
        # Make the request
        ec, data = await self.request(command, data)
        if ec:
            return ec, None
        # Deserialize data
        raw_rows = unpack_table("<32s20s32s", data)
        rows = []
        for ephemkey, address, tx_hash in raw_rows:
            ephemkey = ephemkey[::-1]
            address = address[::-1]
            tx_hash = tx_hash[::-1]
            rows.append((ephemkey, address, tx_hash))
        return ec, rows

    async def total_connections(self):
        """Fetches the total number of server connections."""
        command = b"protocol.total_connections"
        ec, data = await self.request(command, b"")
        if ec:
            return ec, None
        # Deserialize data
        total = struct.unpack("<I", data)[0]
        return ec, total

    async def broadcast(self, raw_tx):
        """Broadcasts a transaction to the network."""
        command = b"protocol.broadcast_transaction"
        ec, _ = await self.request(command, raw_tx)
        return ec

    # Subscribe related stuff -----------------------------------

    async def _base_subscribe_address(self, sub_type, prefix):
        command = b"address.subscribe"

        # prefix = obelisk.Binary.from_string("1011110101")
        # https://wiki.unsystem.net/en/index.php/DarkWallet/Subscriber
        # Prepare parameters.
        # Type. 0 is address, 1 is stealth.
        request_data = struct.pack('B', sub_type)
        # Bitsize
        request_data += struct.pack('B', prefix.size)
        # Blocks
        request_data += prefix.blocks

        # run command
        ec, _ = await self.request(command, request_data)
        if ec:
            return ec, None

        call_later = self.scheduler.add
        subscription = libbitcoin.server.subscribe.Subscription(
            prefix, request_data, self, call_later)
        self._subscribe_manager.add(subscription)

        return ec, subscription

    async def subscribe_address(self, prefix):
        return await self._base_subscribe_address(0, prefix)
    async def subscribe_stealth(self, prefix):
        return await self._base_subscribe_address(1, prefix)

    async def _renew(self, data):
        command = b"address.renew"
        # Server should reply.
        ec, _ = await self.request(command, data, None)
        return ec

    async def _on_update(self, frame):
        *_, data = frame
        # address.update
        # [ version:1 ]
        # [ short_hash:20 ]
        # [ height:4 ]
        # [ blk_hash:32 ]
        # [ tx ]
        # ID is a random number.
        fmt = "<B20sI32s"
        assert struct.calcsize(fmt) == 1 + 20 + 4 + 32 
        split_idx = struct.calcsize(fmt)
        other_data, tx_data = data[:split_idx], data[split_idx:]
        address_version, address_hash, height, block_hash = \
            struct.unpack(fmt, other_data)
        # Now push the result to subscribers.
        result = libbitcoin.server.subscribe.SubscribeResult(
            address_version, address_hash, height, block_hash, tx_data)
        await self._subscribe_manager.update(result)

    async def _on_stealth_update(self, frame):
        # TODO: Unimplemented!
        # address.stealth_update
        # [ bitfield:4 ]
        # [ height:4 ]
        # [ blk_hash:32 ]
        # [ tx ]
        pass

    # -----------------------------------------------------------

