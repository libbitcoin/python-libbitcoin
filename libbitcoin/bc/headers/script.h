typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_data_stack_t bc_data_stack_t;
typedef struct bc_error_code_t bc_error_code_t;
typedef struct bc_hash_digest_t bc_hash_digest_t;
typedef struct bc_operation_t bc_operation_t;
typedef struct bc_operation_list_t bc_operation_list_t;
typedef struct bc_point_list_t bc_point_list_t;
typedef struct bc_short_hash_t bc_short_hash_t;
typedef struct bc_transaction_t bc_transaction_t;

typedef struct bc_script_t bc_script_t;

// Constructor
bc_script_t* bc_create_script();
bc_script_t* bc_create_script_copy(const bc_script_t* other);
bc_script_t* bc_create_script_Ops(const bc_operation_list_t* ops);
bc_script_t* bc_create_script_Data(
    const bc_data_chunk_t* encoded, bool prefix);
// Destructor
void bc_destroy_script(bc_script_t* self);

// Operators
void bc_script__copy(bc_script_t* self, const bc_script_t* other);

bool bc_script__equals(const bc_script_t* self, const bc_script_t* other);
bool bc_script__not_equals(const bc_script_t* self, const bc_script_t* other);

// Deserialization.
bc_script_t* bc_script__factory_from_data(
    const bc_data_chunk_t* encoded, bool prefix);

/// Deserialization invalidates the iterator.
bool bc_script__from_data(bc_script_t* self,
    const bc_data_chunk_t* encoded, bool prefix);

/// Deserialization invalidates the iterator.
void bc_script__from_operations(bc_script_t* self,
    const bc_operation_list_t* ops);
bool bc_script__from_string(bc_script_t* self, const char* mnemonic);

/// A script object is valid if the byte count matches the prefix.
bool bc_script__is_valid(const bc_script_t* self);

/// Script operations is valid if all push ops have the predicated size.
bool bc_script__is_valid_operations(const bc_script_t* self);

// Serialization.
bc_data_chunk_t* bc_script__to_data(const bc_script_t* self, bool prefix);

bc_string_t* bc_script__to_string(
    const bc_script_t* self, uint32_t active_forks);

// Iteration.
bool bc_script__empty(const bc_script_t* self);
size_t bc_script__size(const bc_script_t* self);
bc_operation_t* bc_script__front(const bc_script_t* self);
bc_operation_t* bc_script__back(const bc_script_t* self);
bc_operation_t* bc_script__at(const bc_script_t* self, size_t index);

// Properties (size, accessors, cache).
uint64_t bc_script__satoshi_content_size(const bc_script_t* self);
uint64_t bc_script__serialized_size(const bc_script_t* self, bool prefix);
bc_operation_list_t* bc_script__operations(const bc_script_t* self);

// Signing.

bc_hash_digest_t* bc_script__generate_signature_hash(
    const bc_transaction_t* tx, uint32_t input_index,
    const bc_script_t* script_code, uint8_t sighash_type);

bool bc_script__check_signature(const bc_ec_signature_t* signature,
    uint8_t sighash_type, const bc_data_chunk_t* public_key,
    const bc_script_t* script_code, const bc_transaction_t* tx,
    uint32_t input_index);

bool bc_script__create_endorsement(
    bc_endorsement_t* out, const bc_ec_secret_t* secret,
    const bc_script_t* prevout_script, const bc_transaction_t* tx,
    uint32_t input_index, uint8_t sighash_type);

// Utilities (static).

/// Determine if the fork is enabled in the active forks set.
bool bc_script__is_enabled(uint32_t active_forks,
    bc_rule_fork_t fork);

/// No-code patterns (consensus).
bool bc_script__is_push_only(const bc_operation_list_t* ops);
bool bc_script__is_relaxed_push(const bc_operation_list_t* ops);
bool bc_script__is_coinbase_pattern(
    const bc_operation_list_t* ops, size_t height);

/// Unspendable pattern (standard).
bool bc_script__is_null_data_pattern(const bc_operation_list_t* ops);

/// Payment script patterns (standard, psh is also consensus).
bool bc_script__is_pay_multisig_pattern(const bc_operation_list_t* ops);
bool bc_script__is_pay_public_key_pattern(const bc_operation_list_t* ops);
bool bc_script__is_pay_key_hash_pattern(const bc_operation_list_t* ops);
bool bc_script__is_pay_script_hash_pattern(const bc_operation_list_t* ops);

/// Signature script patterns (standard).
bool bc_script__is_sign_multisig_pattern(const bc_operation_list_t* ops);
bool bc_script__is_sign_public_key_pattern(const bc_operation_list_t* ops);
bool bc_script__is_sign_key_hash_pattern(const bc_operation_list_t* ops);
bool bc_script__is_sign_script_hash_pattern(const bc_operation_list_t* ops);

/// Stack factories (standard).
bc_operation_list_t* bc_script__to_null_data_pattern(
    const bc_data_chunk_t* data);
bc_operation_list_t* bc_script__to_pay_public_key_pattern(
    const bc_data_chunk_t* data);
bc_operation_list_t* bc_script__to_pay_key_hash_pattern(
    const bc_short_hash_t* hash);
bc_operation_list_t* bc_script__to_pay_script_hash_pattern(
    const bc_short_hash_t* hash);
bc_operation_list_t* bc_script__to_pay_multisig_pattern(
    uint8_t signatures, const bc_point_list_t* points);
bc_operation_list_t* bc_script__to_pay_multisig_pattern_DataStack(
    uint8_t signatures, const bc_data_stack_t* points);

// Utilities (non-static).

bc_script_pattern_t bc_script__pattern(const bc_script_t* self);
size_t bc_script__sigops(const bc_script_t* self, bool embedded);
size_t bc_script__embedded_sigops(
    const bc_script_t* self, const bc_script_t* prevout_script);
void bc_script__find_and_delete(
    const bc_script_t* self, const bc_data_stack_t* endorsements);

// Validation.

bc_error_code_t* bc_script__verify(
    const bc_transaction_t* tx, uint32_t input, uint32_t forks);

