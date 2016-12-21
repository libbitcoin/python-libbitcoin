from cffi import FFI
import os
import bc_macros

def read_dir_files(path):
    cdef = ""
    for filename in os.listdir(path):
        if filename.endswith(".h"):
            filename = os.path.join(path, filename)
            cdef += open(filename).read()
    return cdef

cdef = ""

cdef += read_dir_files("enums")
cdef += read_dir_files("headers")

cdef += bc_macros.byte_array("ec_secret")
cdef += bc_macros.byte_array("ec_compressed")
cdef += bc_macros.byte_array("ec_uncompressed")
cdef += bc_macros.byte_array("ec_signature")
cdef += bc_macros.byte_array("payment")
cdef += bc_macros.byte_array("wif_uncompressed")
cdef += bc_macros.byte_array("wif_compressed")
cdef += bc_macros.byte_array("aes_secret")
cdef += bc_macros.byte_array("aes_block")

cdef += bc_macros.hash_type("hash_digest")
cdef += bc_macros.hash_type("half_hash")
cdef += bc_macros.hash_type("quarter_hash")
cdef += bc_macros.hash_type("long_hash")
cdef += bc_macros.hash_type("short_hash")
cdef += bc_macros.hash_type("mini_hash")

cdef += bc_macros.vector("string_list", "bc_string_t")
cdef += bc_macros.vector("operation_list", "bc_operation_t")
cdef += bc_macros.vector("output_info_list", "bc_output_info_t")
cdef += bc_macros.vector("output_list", "bc_output_t")
cdef += bc_macros.vector("input_list", "bc_input_t")
cdef += bc_macros.vector("transaction_list", "bc_transaction_t")
cdef += bc_macros.vector("header_list", "bc_header_t")
cdef += bc_macros.vector("chain_point_list", "bc_point_t")

cdef += bc_macros.int_vector("block_indexes", "size_t")
cdef += bc_macros.int_vector("point_indexes", "uint32_t")
cdef += bc_macros.int_vector("chain_state_bitss", "uint32_t")
cdef += bc_macros.int_vector("chain_state_versions", "uint32_t")
cdef += bc_macros.int_vector("chain_state_timestamps", "uint32_t")

ffibuilder = FFI()
ffibuilder.set_source("_bc", None)
ffibuilder.cdef(cdef)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

