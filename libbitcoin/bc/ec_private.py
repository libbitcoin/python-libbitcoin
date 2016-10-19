from libbitcoin.bc.config import ffi, lib

class EcPrivate:

    mainnet = lib.bc_ec_private__mainnet()
    testnet = lib.bc_ec_private__testnet()

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_ec_private()
        self._obj = obj

    @classmethod
    def from_secret(cls, secret, version=None, compress=True):
        if version is None:
            obj = lib.bc_create_ec_private_Secret(secret._obj)
        elif version is not None and compress:
            obj = lib.bc_create_ec_private_Secret_Version(secret._obj, version)
        elif version is not None and not compress:
            obj = lib.bc_create_ec_private_Secret_Version_nocompress(
                secret._obj, version)
        return cls(obj)

    def __del__(self):
        lib.bc_destroy_ec_private(self._obj)

