from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.string_ import String

libbitcoin_version = ffi.string(lib.bc_libbitcoin_version()).decode()
libbitcoin_major_version = lib.bc_libbitcoin_major_version()
libbitcoin_minor_version = lib.bc_libbitcoin_minor_version()
libbitcoin_patch_version = lib.bc_libbitcoin_patch_version()

