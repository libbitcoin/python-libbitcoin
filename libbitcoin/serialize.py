import struct
import io

import libbitcoin.models

def serialize_hash(hashval):
    return hashval[::-1]

def serialize_uint32(u):
    rs = b""
    rs += struct.pack(b"<I", u & 0xFFFFFFFF)
    return rs

def serialize_point(outpoint):
    r = b""
    r += serialize_hash(outpoint.hash)
    r += serialize_uint32(outpoint.index)
    return r

def deserialize_hash(f):
    return f.read(32)

def deserialize_uint32(f):
    if type(f) is not io.BytesIO:
        f = io.BytesIO(f)

    return struct.unpack(b"<I", f.read(4))[0]

def deserialize_point(f, point):
    if type(f) is not io.BytesIO:
        f = io.BytesIO(f)

    point.hash = deserialize_hash(f)[::-1]
    point.index = deserialize_uint32(f.read(4))

