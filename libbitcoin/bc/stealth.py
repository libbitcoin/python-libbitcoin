from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.elliptic_curve import EcCompressed, EcSecret
from libbitcoin.bc.hash import HashDigest
from libbitcoin.bc.script import Script

ephemeral_public_key_sign = lib.bc_ephemeral_public_key_sign()

# Determine if the script is a null-data script of at least 32 data bytes.
def is_stealth_script(script):
    return lib.bc_is_stealth_script(script._obj) == 1

# Convert a stealth info script to a prefix usable for stealth.
def to_stealth_prefix(script):
    out_prefix = ffi.new("uint32_t*")
    if lib.bc_to_stealth_prefix(out_prefix, script._obj) != 1:
        return None
    return out_prefix[0]

# Create a valid stealth ephemeral private key from the provided seed.
def create_ephemeral_key(seed):
    out_secret = EcSecret()
    seed = DataChunk(seed)
    if lib.bc_create_ephemeral_key(out_secret._obj, seed._obj) != 1:
        return None
    return out_secret

# Create an ephemeral public key from the provided seed with the
# null-data script data value that produces the desired filter prefix.
def create_stealth_data(filter_, seed):
    out_stealth_data = DataChunk()
    out_secret = EcSecret()
    #TODO: unsure how to work with filter and binary type
    assert False

# Extract the stealth ephemeral public key from an output script.
def extract_ephemeral_key(script):
    out_ephemeral_public_key = EcCompressed()
    if lib.bc_extract_ephemeral_key(out_ephemeral_public_key._obj,
                                    script._obj) != 1:
        return None
    return out_ephemeral_public_key

# Extract the unsigned stealth ephemeral public key from an output script.
def extract_ephemeral_key_Hash(script):
    out_unsigned_ephemeral_key = HashDigest()
    if lib.bc_extract_ephemeral_key_Hash(out_unsigned_ephemeral_key._obj,
                                         script._obj) != 1:
        return None
    return out_unsigned_ephemeral_key

# Calculate the shared secret.
def shared_secret(secret, point):
    out_shared = EcSecret()
    if lib.bc_shared_secret(out_shared._obj, secret._obj, point._obj) != 1:
        return None
    return out_shared

def uncover_stealth(ephemeral_or_scan, scan_or_ephemeral, spend):
    # Uncover the stealth public key.
    if isinstance(spend, EcCompressed):
        out_stealth = EcCompressed()
        if lib.bc_uncover_stealth_Public(out_stealth._obj,
            ephemeral_or_scan._obj, scan_or_ephemeral._obj, spend._obj) != 1:
            return None
        return out_stealth
    # Uncover the stealth secret.
    elif isinstance(spend, EcSecret):
        out_stealth = EcSecret()
        if lib.bc_uncover_stealth_Secret(out_stealth._obj,
            ephemeral_or_scan._obj, scan_or_ephemeral._obj, spend._obj) != 1:
            return None
        return out_stealth

