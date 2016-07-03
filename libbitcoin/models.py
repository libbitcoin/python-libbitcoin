import binascii
import struct
import libbitcoin.serialize

class OutPoint:

    def __init__(self):
        self.hash = None
        self.index = None

    def is_null(self):
        return (len(self.hash) == 0) and (self.index == 0xffffffff)

    def _hash_hex(self):
        return str(binascii.hexlify(self.hash), "ascii")

    def __repr__(self):
        return "OutPoint(hash=%s, index=%i)" % (self._hash_hex(), self.index)

    def serialize(self):
        return libbitcoin.serialize.serialize_point(self)

    @staticmethod
    def deserialize(bytes):
        point = OutPoint()
        libbitcoin.serialize.deserialize_output_point(bytes, point)
        return point

    def __eq__(self, other):
        return self.hash == other.hash and self.index == other.index

    def checksum(self):
        hash = self.hash[::-1]
        index_bytes = struct.pack("<I", self.index)
        assert len(hash) == 32
        assert len(index_bytes) == 4
        combined = index_bytes + hash[4:8]
        value = struct.unpack("<Q", combined)[0]
        # value & (2**n - 1) is the same as value % 2**n
        return value & (2**63 - 1)

    def tuple(self):
        return (self._hash_hex(), self.index)

class InPoint(OutPoint):

    def __repr__(self):
        return "InPoint(hash=%s, index=%i)" % (self._hash_hex(), self.index)

    @staticmethod
    def deserialize(bytes):
        point = InPoint()
        libbitcoin.serialize.deserialize_point(bytes, point)
        return point

