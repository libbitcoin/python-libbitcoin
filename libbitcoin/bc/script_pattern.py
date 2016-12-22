from enum import Enum
from libbitcoin.bc.config import lib

class ScriptPattern(Enum):

    null_data = lib.bc_script_pattern__null_data
    pay_multisig = lib.bc_script_pattern__pay_multisig
    pay_public_key = lib.bc_script_pattern__pay_public_key
    pay_key_hash = lib.bc_script_pattern__pay_key_hash
    pay_script_hash = lib.bc_script_pattern__pay_script_hash
    sign_multisig = lib.bc_script_pattern__sign_multisig
    sign_public_key = lib.bc_script_pattern__sign_public_key
    sign_key_hash = lib.bc_script_pattern__sign_key_hash
    sign_script_hash = lib.bc_script_pattern__sign_script_hash
    non_standard = lib.bc_script_pattern__non_standard

