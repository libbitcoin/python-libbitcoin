from cffi import FFI
import os
import bc_macros

def read_from_filenames(filenames):
    cdef = ""
    for filename in filenames:
        cdef += open(filename).read()
    return cdef

def read_dir_files(path):
    filenames = []
    for filename in os.listdir(path):
        if filename.endswith(".h"):
            filename = os.path.join(path, filename)
            filenames.append(filename)
    return read_from_filenames(filenames)

def read_files(path, filenames):
    filenames = [os.path.join(path, filename) for filename in filenames]
    return read_from_filenames(filenames)

cdef = ""

enum_files = [
    "error.h",
    "select_outputs.h",
    "rule_fork.h",
    "opcode.h",
    "sighash_algorithm.h",
    "script_pattern.h"
]
header_files = [
    "error.h",
    "data.h",
    "header.h",
    "dictionary.h",
    "ec_public.h",
    "hd_public.h",
    "select_outputs.h",
    "operation.h",
    "base_10.h",
    "chain_state.h",
    "constants.h",
    "crypto.h",
    "ec_private.h",
    "input.h",
    "binary.h",
    "point.h",
    "machine_number.h",
    "opcode.h",
    "elliptic_curve.h",
    "mnemonic.h",
    "script.h",
    "transaction.h",
    "stealth_address.h",
    "message.h",
    "string.h",
    "version.h",
    "payment_address.h",
    "stealth.h",
    "block.h",
    "hd_private.h",
    "output.h",
    "output_point.h",
    "hash.h"
]

cdef += read_files("enums", enum_files)
cdef += read_files("headers", header_files)

cdef += bc_macros.byte_array("ec_secret")
cdef += bc_macros.byte_array("ec_compressed")
cdef += bc_macros.byte_array("ec_uncompressed")
cdef += bc_macros.byte_array("ec_signature")
cdef += bc_macros.byte_array("payment")
cdef += bc_macros.byte_array("wif_uncompressed")
cdef += bc_macros.byte_array("wif_compressed")
cdef += bc_macros.byte_array("aes_secret")
cdef += bc_macros.byte_array("aes_block")
cdef += bc_macros.byte_array("message_signature")

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
cdef += bc_macros.vector("data_stack", "bc_data_chunk_t")
cdef += bc_macros.vector("point_list", "bc_ec_compressed_t")

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

