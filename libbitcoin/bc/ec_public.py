from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.elliptic_curve import EcCompressed, EcUncompressed

class EcPublic:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_ec_public()
        self._obj = obj

    @classmethod
    def from_string(cls, base16):
        if type(base16) == str:
            base16 = bytes(base16, "ascii")
        obj = lib.bc_create_ec_public_String(base16)
        return cls(obj)

    @classmethod
    def from_compressed(cls, point, compress=True):
        if compress:
            obj = lib.bc_create_ec_public_CompPoint(point._obj)
        else:
            obj = lib.bc_create_ec_public_CompPoint_nocompress(point._obj)
        return cls(obj)

    @classmethod
    def from_uncompressed(cls, point, compress=False):
        if not compress:
            obj = lib.bc_create_ec_public_UncompPoint(point._obj)
        else:
            obj = lib.bc_create_ec_public_UncompPoint_compress(point._obj)
        return cls(obj)

    @classmethod
    def from_point(cls, point):
        if isinstance(point, EcCompressed):
            return cls.from_compressed(point)
        elif isinstance(point, EcUncompressed):
            return cls.from_uncompressed(point)
        else:
            raise Exception("Invalid point type.")

    def __del__(self):
        lib.bc_destroy_ec_public(self._obj)

