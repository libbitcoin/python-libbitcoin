from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.elliptic_curve import EcSecret
from libbitcoin.bc.hd_public import HdPublic
from libbitcoin.bc.string_ import String

class HdPrivate:

    mainnet = lib.bc_hd_private__mainnet()
    testnet = lib.bc_hd_private__testnet()

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_hd_private()
        self._obj = obj

    @classmethod
    def from_seed(cls, seed, prefixes):
        seed = DataChunk(seed)
        obj = lib.bc_create_hd_private_Seed(seed._obj, prefixes)
        return cls(obj)

    @classmethod
    def from_string(cls, encoded):
        if type(encoded) == str:
            encoded = bytes(encoded, "ascii")
        obj = lib.bc_create_hd_private_String(encoded)
        return cls(obj)

    def __del__(self):
        lib.bc_destroy_hd_private(self._obj)

    def encoded(self):
        obj = lib.bc_hd_private__encoded(self._obj)
        return str(String(obj))

    def __str__(self):
        return self.encoded()

    def secret(self):
        obj = lib.bc_hd_private__secret(self._obj)
        return EcSecret(obj)

    def to_public(self):
        obj = lib.bc_hd_private__to_public(self._obj)
        return HdPublic(obj)

    def derive_private(self, index):
        obj = lib.bc_hd_private__derive_private(self._obj, index)
        return HdPrivate(obj)

    def derive_public(self, index):
        obj = lib.bc_hd_private__derive_public(self._obj, index)
        return HdPublic(obj)

