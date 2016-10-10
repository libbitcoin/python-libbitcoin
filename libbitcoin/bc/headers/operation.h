typedef struct bc_operation_stack_t bc_operation_stack_t;
typedef struct bc_point_list_t bc_point_list_t;
typedef struct bc_data_stack_t bc_data_stack_t;
typedef struct bc_short_hash_t bc_short_hash_t;

typedef struct bc_operation_t bc_operation_t;

size_t bc_operation__max_null_data_size();
bc_operation_t* bc_operation__factory_from_data(const bc_data_chunk_t* data);
bool bc_operation__is_push_only(const bc_operation_stack_t* operations);
/// unspendable pattern (standard)
bool bc_operation__is_null_data_pattern(const bc_operation_stack_t* ops);
/// payment script patterns (standard)
bool bc_operation__is_pay_multisig_pattern(const bc_operation_stack_t* ops);
bool bc_operation__is_public_key_pattern(const bc_operation_stack_t* ops);
bool bc_operation__is_pay_key_hash_pattern(const bc_operation_stack_t* ops);
bool bc_operation__is_pay_script_hash_pattern(const bc_operation_stack_t* ops);
/// signature script patterns (standard)
bool bc_operation__is_sign_multisig_pattern(const bc_operation_stack_t* ops);
bool bc_operation__is_sign_public_key_pattern(const bc_operation_stack_t* ops);
bool bc_operation__is_sign_key_hash_pattern(const bc_operation_stack_t* ops);
bool bc_operation__is_sign_script_hash_pattern(const bc_operation_stack_t* ops);
/// stack factories
bc_operation_stack_t* bc_operation__to_null_data_pattern(
    const bc_data_chunk_t* data);
bc_operation_stack_t* bc_operation__to_pay_multisig_pattern_PointList(
    uint8_t signatures,
    const bc_point_list_t* points);
bc_operation_stack_t* bc_operation__to_pay_multisig_pattern(
    uint8_t signatures,
    const bc_data_stack_t* points);
bc_operation_stack_t* bc_operation__to_pay_public_key_pattern(
    const bc_data_chunk_t* point);
bc_operation_stack_t* bc_operation_to_pay_key_hash_pattern(
    const bc_short_hash_t* hash);
bc_operation_stack_t* bc_operation__to_pay_script_hash_pattern(
    const bc_short_hash_t* hash);

bc_operation_t* bc_create_operation();
void bc_destroy_operation(bc_operation_t* self);

// Class members
bool bc_operation__from_data(bc_operation_t* self, const bc_data_chunk_t* data);
bc_data_chunk_t* bc_operation__to_data(const bc_operation_t* self);
bc_string_t* bc_operation__to_string(
    const bc_operation_t* self, uint32_t flags);
bool bc_operation__is_valid(const bc_operation_t* self);
void bc_operation__reset(bc_operation_t* self);
uint64_t bc_operation__serialized_size(const bc_operation_t* self);

bc_opcode_t bc_operation__code(const bc_operation_t* self);
void bc_operation__set_code(bc_operation_t* self, bc_opcode_t code);
bc_data_chunk_t* bc_operation__data(const bc_operation_t* self);
void bc_operation__set_data(bc_operation_t* self, bc_data_chunk_t* data);

