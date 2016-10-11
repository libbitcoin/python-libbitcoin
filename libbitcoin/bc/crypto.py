from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.byte_array import ByteArrayBase, ByteArrayMeta

class AesSecret(ByteArrayBase, metaclass=ByteArrayMeta):
    bc_name = "aes_secret"

class AesBlock(ByteArrayBase, metaclass=ByteArrayMeta):
    bc_name = "aes_block"

aes256_key_size = lib.bc_aes256_key_size()
aes256_block_size = lib.bc_aes256_block_size()

def aes256_encrypt(key, block):
    """Perform aes256 encryption on the specified data block."""
    lib.bc_aes256_encrypt(key._obj, block._obj)

def aes256_decrypt(key, block):
    """Perform aes256 decryption on the specified data block."""
    lib.bc_aes256_decrypt(key._obj, block._obj)

