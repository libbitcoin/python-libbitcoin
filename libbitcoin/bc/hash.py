from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.string_ import String

class HashMeta(type):

    def __new__(cls, clsname, bases, attrs):
        bc_name = attrs["bc_name"]
        def method(method_name, bc_name):
            return getattr(lib, method_name % bc_name)
        attrs["bc_create_hash"] = method("bc_create_%s", bc_name)
        attrs["bc_create_hash_Array"] = method("bc_create_%s_Array", bc_name)
        attrs["bc_destroy_hash"] = method("bc_destroy_%s", bc_name)
        attrs["bc_hash__cdata"] = method("bc_%s__cdata", bc_name)
        attrs["bc_hash__encode_base16"] = method(
            "bc_%s__encode_base16", bc_name)
        attrs["bc_hash__equals"] = method("bc_%s__equals", bc_name)
        return super().__new__(cls, clsname, bases, attrs)

class HashBase:

    def __init__(self, obj=None):
        if obj is None:
            obj = self.bc_create_hash()
        self._obj = obj

    @classmethod
    def from_bytes(cls, data):
        if len(data) != cls.size:
            raise Exception("data is wrong length")
        obj = cls.bc_create_hash_Array(data)
        return cls(obj)

    @classmethod
    def from_string(cls, encoded, reversed_literal=False):
        data = bytes.fromhex(encoded)
        if reversed_literal:
            data = data[::-1]
        return cls.from_bytes(data)

    def __del__(self):
        self.bc_destroy_hash(self._obj)

    def __len__(self):
        return self.size

    @property
    def data(self):
        return ffi.buffer(self.bc_hash__cdata(self._obj), len(self))[:]

    def encode_base16(self):
        obj = self.bc_hash__encode_base16(self._obj)
        return str(String(obj))

    def __eq__(self, other):
        if other is None:
            return False
        return self.bc_hash__equals(self._obj, other._obj) == 1

    def __str__(self):
        return self.data.hex()

    def __repr__(self):
        return "<bc_%s '%s'>" % (self.bc_name, str(self))

class HashDigest(HashBase, metaclass=HashMeta):
    bc_name = "hash_digest"
    size = lib.bc_hash_size()

class HalfHash(HashBase, metaclass=HashMeta):
    bc_name = "half_hash"
    size = lib.bc_half_hash_size()

class QuarterHash(HashBase, metaclass=HashMeta):
    bc_name = "quarter_hash"
    size = lib.bc_quarter_hash_size()

class LongHash(HashBase, metaclass=HashMeta):
    bc_name = "long_hash"
    size = lib.bc_long_hash_size()

class ShortHash(HashBase, metaclass=HashMeta):
    bc_name = "short_hash"
    size = lib.bc_short_hash_size()

class MiniHash(HashBase, metaclass=HashMeta):
    bc_name = "mini_hash"
    size = lib.bc_mini_hash_size()

_null_hash_obj = lib.bc_null_hash()

null_hash = HashDigest(_null_hash_obj)

def bitcoin_hash(data):
    data = DataChunk(data)
    obj = lib.bc_bitcoin_hash(data._obj)
    return HashDigest(obj)

def encode_hash(hash_digest):
    return hash_digest.data[::-1].hex()

def hash_literal(encoded):
    return HashDigest.from_string(encoded, True)

