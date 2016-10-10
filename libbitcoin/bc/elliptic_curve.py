from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.string import String

class ByteArrayMeta(type):

    def __new__(cls, clsname, bases, attrs):
        bc_name = attrs["bc_name"]
        def method(method_name, bc_name):
            return getattr(lib, method_name % bc_name)
        attrs["bc_create_object"] = method("bc_create_%s", bc_name)
        attrs["bc_create_object_Data"] = method("bc_create_%s_Data", bc_name)
        attrs["bc_create_object_Base16"] = method(
            "bc_create_%s_Base16", bc_name)
        attrs["bc_destroy_object"] = method("bc_destroy_%s", bc_name)
        attrs["bc_object__data"] = method("bc_%s__data", bc_name)
        attrs["bc_object__encode_base16"] = method(
            "bc_%s__encode_base16", bc_name)
        def bc_object_size():
            return getattr(lib, "bc_%s_size" % bc_name)()
        attrs["size"] = bc_object_size()
        return super().__new__(cls, clsname, bases, attrs)

class ByteArrayBase:

    def __init__(self, obj=None):
        if obj is None:
            obj = self.bc_create_object()
        self._obj = obj

    @classmethod
    def from_bytes(cls, data):
        obj = cls.bc_create_object_Data(data)
        return cls(obj)

    @classmethod
    def from_string(cls, data, reversed_literal=False):
        if type(data) == str:
            data = bytes.fromhex(data)
        if reversed_literal:
            data = data[::-1]
        return cls.from_bytes(data)

    def __del__(self):
        self.bc_destroy_object(self._obj)

    def __len__(self):
        return self.size

    @property
    def data(self):
        return ffi.buffer(self.bc_object__data(self._obj), len(self))[:]

    def encode_base16(self):
        obj = self.bc_object__encode_base16(self._obj)
        return str(String(obj))

    def __eq__(self, other):
        return self.data == other.data

class EcSecret(ByteArrayBase, metaclass=ByteArrayMeta):
    bc_name = "ec_secret"

    def to_public(self):
        point = EcCompressed()
        if lib.bc_secret_to_public_compressed(point._obj, self._obj) == 0:
            return None
        return point

    def sign(self, sighash):
        signature = EcSignature()
        if lib.bc_sign(signature._obj, self._obj, sighash._obj) == 0:
            return None
        return signature

    def __iadd__(self, secret):
        if lib.bc_ec_add(self._obj, secret._obj) == 0:
            return None
        return self

    def __imul__(self, secret):
        if lib.bc_ec_multiply(self._obj, secret._obj) == 0:
            return None
        return self

class EcCompressed(ByteArrayBase, metaclass=ByteArrayMeta):
    bc_name = "ec_compressed"

    def decompress(self):
        out = EcUncompressed()
        if lib.bc_decompress(out._obj, self._obj) == 0:
            return None
        return out

    def verify(self, hash_, signature):
        return lib.bc_verify_signature_compressed(self._obj, hash_._obj,
                                                  signature._obj) == 1

    def __iadd__(self, secret):
        if lib.bc_ec_add_compressed(self._obj, secret._obj) == 0:
            return None
        return self

    def __imul__(self, secret):
        if lib.bc_ec_multiply_compressed(self._obj, secret._obj) == 0:
            return None
        return self

class EcUncompressed(ByteArrayBase, metaclass=ByteArrayMeta):
    bc_name = "ec_uncompressed"

class EcSignature(ByteArrayBase, metaclass=ByteArrayMeta):
    bc_name = "ec_signature"

    @classmethod
    def from_der(cls, data, strict):
        der = DataChunk(data)
        out = EcSignature()
        if lib.bc_parse_signature(out._obj, der._obj, strict) == 0:
            return None
        return out

    def encode(self):
        out = DataChunk()
        if lib.bc_encode_signature(out._obj, self._obj) == 0:
            return None
        return out.data

