typedef enum bc_console_result_t
{
    bc_console_result__failure = -1,
    bc_console_result__okay = 0,
    bc_console_result__invalid = 1

} bc_console_result_t;

// The numeric values of these codes may change without notice.
typedef enum bc_error_t
{
    bc_error__success = 0,

    // network errors
    bc_error__service_stopped,
    bc_error__operation_failed,

    // blockchain errors
    bc_error__not_found,
    bc_error__duplicate,
    bc_error__orphan,
    bc_error__unsupported_script_pattern,

    // network errors (more)
    bc_error__resolve_failed,
    bc_error__network_unreachable,
    bc_error__address_in_use,
    bc_error__listen_failed,
    bc_error__accept_failed,
    bc_error__bad_stream,
    bc_error__channel_timeout,

    // transaction pool
    bc_error__blockchain_reorganized,
    bc_error__pool_filled,

    // validate tx
    bc_error__coinbase_transaction,
    bc_error__is_not_standard,
    bc_error__double_spend,
    bc_error__input_not_found,

    // check_transaction()
    bc_error__empty_transaction,
    bc_error__spend_overflow,
    bc_error__invalid_coinbase_script_size,
    bc_error__previous_output_null,

    // validate block
    bc_error__previous_block_invalid,

    // check_block()
    bc_error__size_limits,
    bc_error__invalid_proof_of_work,
    bc_error__futuristic_timestamp,
    bc_error__first_not_coinbase,
    bc_error__extra_coinbases,
    bc_error__too_many_sigs,
    bc_error__merkle_mismatch,

    // accept_block()
    bc_error__incorrect_proof_of_work,
    bc_error__timestamp_too_early,
    bc_error__non_final_transaction,
    bc_error__checkpoints_failed,
    bc_error__old_version_block,
    bc_error__coinbase_height_mismatch,

    // connect_block()
    bc_error__unspent_duplicate,
    bc_error__validate_inputs_failed,
    bc_error__spend_exceeds_value,
    bc_error__coinbase_too_large,

    // file system errors
    bc_error__file_system,

    // unknown errors
    bc_error__unknown,

    // network errors (more)
    bc_error__address_blocked,
    bc_error__channel_stopped,

    // check_transaction() (more)
    bc_error__coinbase_maturity,

    // check_block() (more)
    bc_error__empty_block,
    bc_error__insufficient_work

} bc_error_t;

