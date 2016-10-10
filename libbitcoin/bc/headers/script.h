typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_error_code_t bc_error_code_t;
typedef struct bc_hash_digest_t bc_hash_digest_t;
typedef struct bc_operation_stack_t bc_operation_stack_t;

// Forward declaration for methods below.
typedef struct bc_transaction_t bc_transaction_t;

typedef struct bc_script_t bc_script_t;
// Static functions
bc_script_t* bc_script__factory_from_data(const bc_data_chunk_t* data,
    bool prefix, bc_script_parse_mode_t mode);

bool bc_script__is_enabled(uint32_t active_forks, bc_rule_fork_t flag);
bc_hash_digest_t* bc_script__generate_signature_hash(
    const bc_transaction_t* parent_tx, uint32_t input_index,
    const bc_script_t* script_code, uint8_t sighash_type);
bool bc_script__create_endorsement(
    bc_endorsement_t* out, const bc_ec_secret_t* secret,
    const bc_script_t* prevout_script, const bc_transaction_t* new_tx,
    uint32_t input_index, uint8_t sighash_type);
bool bc_script__check_signature(const bc_ec_signature_t* signature,
    uint8_t sighash_type, const bc_data_chunk_t* public_key,
    const bc_script_t* script_code, const bc_transaction_t* parent_tx,
    uint32_t input_index);
bc_error_code_t* bc_script__verify(
    const bc_transaction_t* tx, uint32_t input_index,
    uint32_t flags);
bc_error_code_t* bc_script__verify_Script(
    const bc_transaction_t* tx, uint32_t input_index,
    const bc_script_t* prevout_script, uint32_t flags);

// Constructor
bc_script_t* bc_create_script();
// Destructor
void bc_destroy_script(bc_script_t* self);

// Member functions
bc_script_pattern_t bc_script__pattern(const bc_script_t* self);
bool bc_script__is_raw_data(const bc_script_t* self);
bool bc_script__from_data(bc_script_t* self, const bc_data_chunk_t* data,
    bool prefix, bc_script_parse_mode_t mode);
bc_data_chunk_t* bc_script__to_data(const bc_script_t* self, bool prefix);

bool bc_script__from_string(bc_script_t* self, const char* human_readable);
bc_string_t* bc_script__to_string(const bc_script_t* self, uint32_t flags);
bool bc_script__is_valid(const bc_script_t* self);
void bc_script__reset(bc_script_t* self);
size_t bc_script__pay_script_hash_sigops(const bc_script_t* self,
    const bc_script_t* prevout);
size_t bc_script__sigops(const bc_script_t* self, bool serialized_script);
uint64_t bc_script__satoshi_content_size(const bc_script_t* self);
uint64_t bc_script__serialized_size(const bc_script_t* self, bool prefix);

// Member variables
bc_operation_stack_t* bc_script__operations(const bc_script_t* self);
void bc_script__set_operations(bc_script_t* self,
    const bc_operation_stack_t* operations);

