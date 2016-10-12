typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_error_code_t bc_error_code_t;
typedef struct bc_hash_digest_t bc_hash_digest_t;
typedef struct bc_hash_number_t bc_hash_number_t;
typedef struct bc_header_t bc_header_t;
typedef struct bc_transaction_list_t bc_transaction_list_t;

// Immutable vector of size_t
typedef struct bc_block_indexes_t bc_block_indexes_t;
// Constructor
bc_block_indexes_t* bc_create_block_indexes(
    const size_t* indexes, size_t size);
// Destructor
void bc_destroy_block_indexes(bc_block_indexes_t* self);
// Member functions
size_t bc_block_indexes_size(const bc_block_indexes_t* self);
size_t bc_block_indexes_at(const bc_block_indexes_t* self, size_t pos);

typedef struct bc_block_t bc_block_t;

// Static functions
bc_block_t* bc_block__factory_from_data(
    const bc_data_chunk_t* data);
bc_block_t* bc_block__factory_from_data_without_transaction_count(
    const bc_data_chunk_t* data);

bool bc_block__is_retarget_height(size_t height);
bc_hash_number_t* bc_block__difficulty_Static(uint32_t bits);
uint32_t bc_block__work_required(uint64_t timespan, uint32_t bits);
uint64_t bc_block__subsidy(size_t height);
size_t bc_block__locator_size(size_t top);
bc_block_indexes_t* bc_block__locator_heights(size_t top);
bc_block_t* bc_block__genesis_mainnet();
bc_block_t* bc_block__genesis_testnet();

// Constructor
bc_block_t* bc_create_block();
bc_block_t* bc_create_block_copy(const bc_block_t* other);
bc_block_t* bc_create_block_Options(
    const bc_header_t* header,
    const bc_transaction_list_t* transactions);

// Destructor
void bc_destroy_block(const bc_block_t* self);

// Member functions
bool bc_block__from_data(
    bc_block_t* self, const bc_data_chunk_t* data);
bool bc_block__from_data_without_transaction_count(
    bc_block_t* self, const bc_data_chunk_t* data);
bc_data_chunk_t* bc_block__to_data(const bc_block_t* self);
bc_data_chunk_t* bc_block__to_data_without_transaction_count(
    const bc_block_t* self);

bool bc_block__is_valid(const bc_block_t* self);
bool bc_block__is_extra_coinbases(const bc_block_t* self);
bool bc_block__is_valid_merkle_root(const bc_block_t* self);
bool bc_block__is_distinct_transaction_set(const bc_block_t* self);
bool bc_block__is_valid_coinbase_claim(const bc_block_t* self, size_t height);
bool bc_block__is_valid_coinbase_script(const bc_block_t* self, size_t height);

void bc_block__reset(bc_block_t* self);
bc_hash_digest_t* bc_block__hash(const bc_block_t* self);

bc_error_code_t* bc_block__check(const bc_block_t* self);
bc_error_code_t* bc_block__check_transactions(const bc_block_t* self);
bc_error_code_t* bc_block__accept(
    const bc_block_t* self, const bc_chain_state_t* state);
bc_error_code_t* bc_block__accept_transactions(
    const bc_block_t* self, const bc_chain_state_t* state);
bc_error_code_t* bc_block__connect(
    const bc_block_t* self, const bc_chain_state_t* state);
bc_error_code_t* bc_block__connect_transactions(
    const bc_block_t* self, const bc_chain_state_t* state);

uint64_t bc_block__fees(const bc_block_t* self);
uint64_t bc_block__claim(const bc_block_t* self);
uint64_t bc_block__reward(const bc_block_t* self, size_t height);

size_t bc_block__total_inputs(const bc_block_t* self);
bc_hash_number_t* bc_block__difficulty(const bc_block_t* self);
bc_hash_digest_t* bc_block__generate_merkle_root(const bc_block_t* self);
uint64_t bc_block__serialized_size(const bc_block_t* self);
uint64_t bc_block__serialized_size_without_transaction_count(
    const bc_block_t* self);
size_t bc_block__signature_operations(
    const bc_block_t* self, bool bip16_active);

// Member variables
bc_header_t* bc_block__header(const bc_block_t* self);
void bc_block__set_header(bc_block_t* self, const bc_header_t* header);
bc_transaction_list_t* bc_block__transactions(const bc_block_t* self);
void bc_block__set_transactions(bc_block_t* self,
    const bc_transaction_list_t* transactions);

