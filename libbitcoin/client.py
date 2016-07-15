import random
import struct
import enum
import asyncio
import zmq
import libbitcoin
import libbitcoin.serialize
import libbitcoin.bitcoin_utils
import libbitcoin.subscribe

def create_random_id():
    MAX_UINT32 = 4294967295
    return random.randint(0, MAX_UINT32)

def make_error_code(ec):
    if not ec:
        return None
    return libbitcoin.ErrorCode(ec)

def pack_block_index(index):
    if type(index) == bytes:
        assert len(index) == 32
        return libbitcoin.serialize.serialize_hash(index)
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

class Settings:

    def __init__(self):
        self.renew_time = 5 * 60

class Client:

    def __init__(self, address, context, settings=Settings()):
        self._address = address
        self._context = context
        self.settings = settings
        self._setup_socket()

        self._subscribe_manager = libbitcoin.subscribe.SubscribeManager()

    def _setup_socket(self):
        self._socket = self._context.zmq_context.socket(zmq.DEALER)
        self._socket.connect(self._address)
        self._context.poller.register(self._socket)
        self._context.poller.add_handler(b"address.update", self._on_update)

    async def _send_request(self, command, request_id, data):
        request = [
            command,
            struct.pack("<I", request_id),
            data
        ]
        await self._socket.send_multipart(request)

    async def request(self, request_command, request_data, expiry_time=None):
        future = self._context.Future()
        request_id = create_random_id()
        self._context.poller.add_future(request_id, future)

        await self._send_request(request_command, request_id, request_data)

        reply = await future
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
        return ec, data

    async def history(self, address, from_height=0):
        """Fetches history for an address. cb is a callback which
        accepts an error code, and a list of rows consisting of:

            id (obelisk.PointIdent.output or spend)
            point (hash and index)
            block height
            value / checksum

        If the row is for an output then the last item is the value.
        Otherwise it is a checksum of the previous output point, so
        spends can be matched to the rows they spend.
        Use outpoint.spend_checksum() to compute output point checksums."""

        command = b"address.fetch_history2"

        address_version, address_hash = \
            libbitcoin.bitcoin_utils.bc_address_to_hash_160(address)

        # prepare parameters
        data = struct.pack('B', address_version)    # address version
        data += address_hash                        # address
        data += struct.pack('<I', from_height)      # from_height

        ec, data = await self.request(command, data)

        # parse results
        rows = unpack_table("<B32sIIQ", data)
        history = []
        for id, hash, index, height, value in rows:
            id = PointIdent(id)
            if id == PointIdent.output:
                point = libbitcoin.models.OutPoint()
            elif id == PointIdent.spend:
                point = libbitcoin.models.InPoint()
            point.hash = hash[::-1]
            point.index = index
            history.append((point, height, value))

        return ec, history

    async def last_height(self):
        """Fetches the height of the last block in our blockchain."""
        command = b"blockchain.fetch_last_height"
        ec, data = await self.request(command, b"")
        # Deserialize data
        height = struct.unpack("<I", data)[0]
        return ec, height

    async def transaction(self, tx_hash):
        """Fetches a transaction by hash from the blockchain."""
        command = b"blockchain.fetch_transaction"
        data = libbitcoin.serialize.serialize_hash(tx_hash)
        ec, data = await self.request(command, data)
        return ec, data

    async def transaction_from_pool(self, tx_hash):
        """Fetches a transaction by hash from the transaction pool."""
        command = b"transaction_pool.fetch_transaction"
        data = libbitcoin.serialize.serialize_hash(tx_hash)
        ec, data = await self.request(command, data)
        return ec, data

    async def spend(self, outpoint):
        """Fetches a corresponding spend of an output."""
        command = b"blockchain.fetch_spend"
        data = outpoint.serialize()
        ec, data = await self.request(command, data)
        spend = libbitcoin.models.InPoint.deserialize(data)
        return ec, spend

    async def transaction_index(self, tx_hash):
        """Fetch the block height that contains a transaction and its index
        within a block."""
        command = b"blockchain.fetch_transaction_index"
        data = libbitcoin.serialize.serialize_hash(tx_hash)
        ec, data = await self.request(command, data)
        height, index = struct.unpack("<II", data)
        return ec, height, index

    async def block_transaction_hashes(self, block_hash):
        """Fetches list of transaction hashes in a block by block hash."""
        command = b"blockchain.fetch_block_transaction_hashes"
        data = libbitcoin.serialize.serialize_hash(block_hash)
        ec, data = await self.request(command, data)
        rows = unpack_table("32s", data)
        hashes = [row[0][::-1] for row in rows]
        return ec, hashes

    async def block_height(self, block_hash):
        """Fetches the height of a block given its hash."""
        command = b"blockchain.fetch_block_height"
        data = libbitcoin.serialize.serialize_hash(block_hash)
        ec, data = await self.request(command, data)
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
        """Fetches the total number of connections."""
        command = b"protocol.total_connections"
        ec, data = await self.request(command, b"")
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

        subscription = libbitcoin.subscribe.Subscription(
            prefix, request_data, self)
        self._subscribe_manager.add(subscription)

        return ec, subscription

    async def subscribe_address(self, prefix):
        return await self._base_subscribe_address(0, prefix)
    async def subscribe_stealth(self, prefix):
        return await self._base_subscribe_address(1, prefix)

    async def _renew(self, data):
        command = b"address.renew"
        # Server should reply.
        ec, _ = await self.request(command, data)
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
        result = libbitcoin.subscribe.SubscribeResult(
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

