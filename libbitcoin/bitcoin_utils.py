import hashlib

bitcoin_hash = lambda x: hashlib.sha256(hashlib.sha256(x).digest()).digest()

def hash_160(public_key):
    try:
        md = hashlib.new('ripemd160')
        md.update(hashlib.sha256(public_key).digest())
        return md.digest()
    except:
        import ripemd
        md = ripemd.new(hashlib.sha256(public_key).digest())
        return md.digest()

def bc_address_to_hash_160(addr):
    bytes = b58decode(addr, 25)
    return bytes[0], bytes[1:21]

def hash_160_to_bc_address(addrtype, h160):
    vh160 = bytes([addrtype]) + h160
    h = bitcoin_hash(vh160)
    addr = vh160 + h[0:4]
    return b58encode(addr)

__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

def b58decode(v, length):
    """ decode v into a string of len bytes."""
    long_value = 0
    for (i, c) in enumerate(v[::-1]):
        long_value += __b58chars.find(c) * (__b58base**i)

    result = b""
    while long_value >= 256:
        div, mod = divmod(long_value, 256)
        result = bytes([mod]) + result
        long_value = div
    result = bytes([long_value]) + result

    nPad = 0
    for c in v:
        if c == __b58chars[0]:
            nPad += 1
        else:
            break

    result = bytes([0]) * nPad + result
    if length is not None and len(result) != length:
        return None

    return result

def b58encode(v):
    """ encode v, which is a string of bytes, to base58."""

    long_value = 0
    for (i, c) in enumerate(v[::-1]):
        long_value += (256**i) * c

    result = ""
    while long_value >= __b58base:
        div, mod = divmod(long_value, __b58base)
        result = __b58chars[mod] + result
        long_value = div
    result = __b58chars[long_value] + result

    # Bitcoin does a little leading-zero-compression:
    # leading 0-bytes in the input become leading-1s
    nPad = 0
    for c in v:
        if c == 0:
            nPad += 1
        else:
            break

    return (__b58chars[0] * nPad) + result

if __name__ == "__main__":
    address = "15s5nojkHKxJz3GvpKD1S6DR9nKUxSzNko"
    version, hash = bc_address_to_hash_160(address)
    address2 = hash_160_to_bc_address(version, hash)
    print(address2)
    assert address == address2

