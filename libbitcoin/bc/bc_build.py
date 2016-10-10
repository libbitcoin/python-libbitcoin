from cffi import FFI
import os
import bc_macros

cdef = ""
for filename in os.listdir("headers"):
    if filename.endswith(".h"):
        filename = os.path.join("headers", filename)
        cdef += open(filename).read()

cdef += bc_macros.byte_array("ec_secret")
cdef += bc_macros.byte_array("ec_compressed")
cdef += bc_macros.byte_array("ec_uncompressed")
cdef += bc_macros.byte_array("ec_signature")
cdef += bc_macros.byte_array("payment")

cdef += bc_macros.hash_type("hash_digest")
cdef += bc_macros.hash_type("half_hash")
cdef += bc_macros.hash_type("quarter_hash")
cdef += bc_macros.hash_type("long_hash")
cdef += bc_macros.hash_type("short_hash")
cdef += bc_macros.hash_type("mini_hash")

ffibuilder = FFI()
ffibuilder.set_source("_bc", None)
ffibuilder.cdef(cdef)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

