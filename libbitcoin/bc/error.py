from enum import Enum
from libbitcoin.bc.config import lib
from libbitcoin.bc.string_ import String

class ConsoleResult(Enum):
    failure = lib.bc_console_result__failure
    okay = lib.bc_console_result__okay
    invalid = lib.bc_console_result__invalid

class Error(Enum):
    success = lib.bc_error__success
    deprecated = lib.bc_error__deprecated
    unknown = lib.bc_error__unknown
    not_found = lib.bc_error__not_found
    file_system = lib.bc_error__file_system
    non_standard = lib.bc_error__non_standard
    service_stopped = lib.bc_error__service_stopped
    operation_failed = lib.bc_error__operation_failed
    resolve_failed = lib.bc_error__resolve_failed
    network_unreachable = lib.bc_error__network_unreachable
    address_in_use = lib.bc_error__address_in_use
    listen_failed = lib.bc_error__listen_failed
    accept_failed = lib.bc_error__accept_failed
    bad_stream = lib.bc_error__bad_stream
    channel_timeout = lib.bc_error__channel_timeout
    address_blocked = lib.bc_error__address_blocked
    channel_stopped = lib.bc_error__channel_stopped
    store_block_duplicate = lib.bc_error__store_block_duplicate
    store_block_invalid_height = lib.bc_error__store_block_invalid_height
    store_block_missing_parent = lib.bc_error__store_block_missing_parent
    duplicate_block = lib.bc_error__duplicate_block
    orphan_block = lib.bc_error__orphan_block
    invalid_previous_block = lib.bc_error__invalid_previous_block
    insufficient_work = lib.bc_error__insufficient_work
    blockchain_reorganized = lib.bc_error__blockchain_reorganized
    transaction_pool_filled = lib.bc_error__transaction_pool_filled
    duplicate_pool_transaction = lib.bc_error__duplicate_pool_transaction
    invalid_proof_of_work = lib.bc_error__invalid_proof_of_work
    futuristic_timestamp = lib.bc_error__futuristic_timestamp
    checkpoints_failed = lib.bc_error__checkpoints_failed
    old_version_block = lib.bc_error__old_version_block
    incorrect_proof_of_work = lib.bc_error__incorrect_proof_of_work
    timestamp_too_early = lib.bc_error__timestamp_too_early
    block_size_limit = lib.bc_error__block_size_limit
    empty_block = lib.bc_error__empty_block
    first_not_coinbase = lib.bc_error__first_not_coinbase
    extra_coinbases = lib.bc_error__extra_coinbases
    internal_duplicate = lib.bc_error__internal_duplicate
    internal_double_spend = lib.bc_error__internal_double_spend
    merkle_mismatch = lib.bc_error__merkle_mismatch
    block_legacy_sigop_limit = lib.bc_error__block_legacy_sigop_limit
    non_final_transaction = lib.bc_error__non_final_transaction
    coinbase_height_mismatch = lib.bc_error__coinbase_height_mismatch
    coinbase_value_limit = lib.bc_error__coinbase_value_limit
    block_embedded_sigop_limit = lib.bc_error__block_embedded_sigop_limit
    empty_transaction = lib.bc_error__empty_transaction
    previous_output_null = lib.bc_error__previous_output_null
    spend_overflow = lib.bc_error__spend_overflow
    invalid_coinbase_script_size = lib.bc_error__invalid_coinbase_script_size
    coinbase_transaction = lib.bc_error__coinbase_transaction
    transction_size_limit = lib.bc_error__transction_size_limit
    transaction_legacy_sigop_limit = lib.bc_error__transaction_legacy_sigop_limit
    unspent_duplicate = lib.bc_error__unspent_duplicate
    missing_previous_output = lib.bc_error__missing_previous_output
    double_spend = lib.bc_error__double_spend
    coinbase_maturity = lib.bc_error__coinbase_maturity
    spend_exceeds_value = lib.bc_error__spend_exceeds_value
    transaction_embedded_sigop_limit = lib.bc_error__transaction_embedded_sigop_limit
    invalid_script = lib.bc_error__invalid_script
    invalid_script_size = lib.bc_error__invalid_script_size
    invalid_push_data_size = lib.bc_error__invalid_push_data_size
    invalid_operation_count = lib.bc_error__invalid_operation_count
    invalid_stack_size = lib.bc_error__invalid_stack_size
    invalid_stack_scope = lib.bc_error__invalid_stack_scope
    invalid_script_embed = lib.bc_error__invalid_script_embed
    invalid_signature_encoding = lib.bc_error__invalid_signature_encoding
    invalid_signature_lax_encoding = lib.bc_error__invalid_signature_lax_encoding
    incorrect_signature = lib.bc_error__incorrect_signature
    stack_false = lib.bc_error__stack_false
    op_disabled = lib.bc_error__op_disabled
    op_reserved = lib.bc_error__op_reserved
    op_push_size = lib.bc_error__op_push_size
    op_push_data = lib.bc_error__op_push_data
    op_if = lib.bc_error__op_if
    op_notif = lib.bc_error__op_notif
    op_else = lib.bc_error__op_else
    op_endif = lib.bc_error__op_endif
    op_verify1 = lib.bc_error__op_verify1
    op_verify2 = lib.bc_error__op_verify2
    op_return = lib.bc_error__op_return
    op_to_alt_stack = lib.bc_error__op_to_alt_stack
    op_from_alt_stack = lib.bc_error__op_from_alt_stack
    op_drop2 = lib.bc_error__op_drop2
    op_dup2 = lib.bc_error__op_dup2
    op_dup3 = lib.bc_error__op_dup3
    op_over2 = lib.bc_error__op_over2
    op_rot2 = lib.bc_error__op_rot2
    op_swap2 = lib.bc_error__op_swap2
    op_if_dup = lib.bc_error__op_if_dup
    op_drop = lib.bc_error__op_drop
    op_dup = lib.bc_error__op_dup
    op_nip = lib.bc_error__op_nip
    op_over = lib.bc_error__op_over
    op_pick = lib.bc_error__op_pick
    op_roll = lib.bc_error__op_roll
    op_rot = lib.bc_error__op_rot
    op_swap = lib.bc_error__op_swap
    op_tuck = lib.bc_error__op_tuck
    op_size = lib.bc_error__op_size
    op_equal = lib.bc_error__op_equal
    op_equal_verify1 = lib.bc_error__op_equal_verify1
    op_equal_verify2 = lib.bc_error__op_equal_verify2
    op_add1 = lib.bc_error__op_add1
    op_sub1 = lib.bc_error__op_sub1
    op_negate = lib.bc_error__op_negate
    op_abs = lib.bc_error__op_abs
    op_not = lib.bc_error__op_not
    op_nonzero = lib.bc_error__op_nonzero
    op_add = lib.bc_error__op_add
    op_sub = lib.bc_error__op_sub
    op_bool_and = lib.bc_error__op_bool_and
    op_bool_or = lib.bc_error__op_bool_or
    op_num_equal = lib.bc_error__op_num_equal
    op_num_equal_verify1 = lib.bc_error__op_num_equal_verify1
    op_num_equal_verify2 = lib.bc_error__op_num_equal_verify2
    op_num_not_equal = lib.bc_error__op_num_not_equal
    op_less_than = lib.bc_error__op_less_than
    op_greater_than = lib.bc_error__op_greater_than
    op_less_than_or_equal = lib.bc_error__op_less_than_or_equal
    op_greater_than_or_equal = lib.bc_error__op_greater_than_or_equal
    op_min = lib.bc_error__op_min
    op_max = lib.bc_error__op_max
    op_within = lib.bc_error__op_within
    op_ripemd160 = lib.bc_error__op_ripemd160
    op_sha1 = lib.bc_error__op_sha1
    op_sha256 = lib.bc_error__op_sha256
    op_hash160 = lib.bc_error__op_hash160
    op_hash256 = lib.bc_error__op_hash256
    op_code_seperator = lib.bc_error__op_code_seperator
    op_check_sig_verify1 = lib.bc_error__op_check_sig_verify1
    op_check_sig = lib.bc_error__op_check_sig
    op_check_multisig_verify1 = lib.bc_error__op_check_multisig_verify1
    op_check_multisig_verify2 = lib.bc_error__op_check_multisig_verify2
    op_check_multisig_verify3 = lib.bc_error__op_check_multisig_verify3
    op_check_multisig_verify4 = lib.bc_error__op_check_multisig_verify4
    op_check_multisig_verify5 = lib.bc_error__op_check_multisig_verify5
    op_check_multisig_verify6 = lib.bc_error__op_check_multisig_verify6
    op_check_multisig_verify7 = lib.bc_error__op_check_multisig_verify7
    op_check_multisig = lib.bc_error__op_check_multisig
    op_check_locktime_verify1 = lib.bc_error__op_check_locktime_verify1
    op_check_locktime_verify2 = lib.bc_error__op_check_locktime_verify2
    op_check_locktime_verify3 = lib.bc_error__op_check_locktime_verify3
    op_check_locktime_verify4 = lib.bc_error__op_check_locktime_verify4
    op_check_locktime_verify5 = lib.bc_error__op_check_locktime_verify5
    op_check_locktime_verify6 = lib.bc_error__op_check_locktime_verify6

class ErrorCode:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_error_code_default()
        elif isinstance(obj, Error):
            obj = lib.bc_create_error_code(obj.value)
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_error_code(self._obj)

    def message(self):
        obj = lib.bc_error_code__message(self._obj)
        return str(String(obj))

    def __str__(self):
        return self.message()

    def __repr__(self):
        return "<bc_error_code '%s'>" % str(self)

    def is_valid(self):
        return lib.bc_error_code__is_valid(self._obj) == 1

    def __eq__(self, ec):
        return lib.bc_error_code__equals(self._obj, ec.value) == 1

