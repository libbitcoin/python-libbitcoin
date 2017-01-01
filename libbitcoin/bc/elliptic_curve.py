from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.byte_array import ByteArrayBase, ByteArrayMeta
from libbitcoin.bc.vector import VectorMeta, VectorBase

class Endorsement(DataChunk):

    @staticmethod
    def max_size():
        return lib.bc_max_endorsement_size()

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
        return signature.data

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
        if isinstance(signature, bytes):
            signature = EcSignature.from_bytes(signature)
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

class PointList(VectorBase, metaclass=VectorMeta):
    bc_name = "point_list"
    item_type = EcCompressed

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

