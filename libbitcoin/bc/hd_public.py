from libbitcoin.bc.config import lib
from libbitcoin.bc.elliptic_curve import EcCompressed
from libbitcoin.bc.string import String

hd_first_hardened_key = lib.bc_hd_first_hardened_key()

class HdPublic:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_hd_public()
        self._obj = obj

    @classmethod
    def from_string(cls, encoded):
        if type(encoded) == str:
            encoded = bytes(encoded, "ascii")
        obj = lib.bc_create_hd_public_String(encoded)
        return cls(obj)

    def __del__(self):
        lib.bc_destroy_hd_public(self._obj)

    def is_valid(self):
        return lib.bc_hd_public__is_valid(self._obj) == 1

    def encoded(self):
        obj = lib.bc_hd_public__encoded(self._obj)
        return str(String(obj))

    def point(self):
        obj = lib.bc_hd_public__point(self._obj)
        return EcCompressed(obj).data

    def derive_public(self, index):
        obj = lib.bc_hd_public__derive_public(self._obj, index)
        return HdPublic(obj)

