from enum import Enum
from libbitcoin.bc.config import lib
from libbitcoin.bc.string import String

class ConsoleResult(Enum):
    failure = lib.bc_console_result__failure
    okay = lib.bc_console_result__okay
    invalid = lib.bc_console_result__invalid

class Error(Enum):
    success = lib.bc_error__success
    service_stopped = lib.bc_error__service_stopped
    operation_failed = lib.bc_error__operation_failed
    not_found = lib.bc_error__not_found
    duplicate = lib.bc_error__duplicate
    orphan = lib.bc_error__orphan
    unsupported_script_pattern = lib.bc_error__unsupported_script_pattern
    resolve_failed = lib.bc_error__resolve_failed
    network_unreachable = lib.bc_error__network_unreachable
    address_in_use = lib.bc_error__address_in_use
    listen_failed = lib.bc_error__listen_failed
    accept_failed = lib.bc_error__accept_failed
    bad_stream = lib.bc_error__bad_stream
    channel_timeout = lib.bc_error__channel_timeout
    blockchain_reorganized = lib.bc_error__blockchain_reorganized
    pool_filled = lib.bc_error__pool_filled
    coinbase_transaction = lib.bc_error__coinbase_transaction
    is_not_standard = lib.bc_error__is_not_standard
    double_spend = lib.bc_error__double_spend
    input_not_found = lib.bc_error__input_not_found
    empty_transaction = lib.bc_error__empty_transaction
    spend_overflow = lib.bc_error__spend_overflow
    invalid_coinbase_script_size = lib.bc_error__invalid_coinbase_script_size
    previous_output_null = lib.bc_error__previous_output_null
    previous_block_invalid = lib.bc_error__previous_block_invalid
    size_limits = lib.bc_error__size_limits
    invalid_proof_of_work = lib.bc_error__invalid_proof_of_work
    futuristic_timestamp = lib.bc_error__futuristic_timestamp
    first_not_coinbase = lib.bc_error__first_not_coinbase
    extra_coinbases = lib.bc_error__extra_coinbases
    too_many_sigs = lib.bc_error__too_many_sigs
    merkle_mismatch = lib.bc_error__merkle_mismatch
    incorrect_proof_of_work = lib.bc_error__incorrect_proof_of_work
    timestamp_too_early = lib.bc_error__timestamp_too_early
    non_final_transaction = lib.bc_error__non_final_transaction
    checkpoints_failed = lib.bc_error__checkpoints_failed
    old_version_block = lib.bc_error__old_version_block
    coinbase_height_mismatch = lib.bc_error__coinbase_height_mismatch
    unspent_duplicate = lib.bc_error__unspent_duplicate
    validate_inputs_failed = lib.bc_error__validate_inputs_failed
    spend_exceeds_value = lib.bc_error__spend_exceeds_value
    coinbase_too_large = lib.bc_error__coinbase_too_large
    file_system = lib.bc_error__file_system
    unknown = lib.bc_error__unknown
    address_blocked = lib.bc_error__address_blocked
    channel_stopped = lib.bc_error__channel_stopped
    coinbase_maturity = lib.bc_error__coinbase_maturity
    empty_block = lib.bc_error__empty_block
    insufficient_work = lib.bc_error__insufficient_work

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

