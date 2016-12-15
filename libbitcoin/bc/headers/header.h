typedef struct bc_chain_state_t bc_chain_state_t;
typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_error_code_t bc_error_code_t;
typedef struct bc_hash_digest_t bc_hash_digest_t;

typedef struct bc_header_t bc_header_t;

// Constructor
bc_header_t* bc_create_header();
bc_header_t* bc_create_header_copy(const bc_header_t* other);
bc_header_t* bc_create_header_copy_with_Hash(const bc_header_t* other,
    const bc_hash_digest_t* hash);
bc_header_t* bc_create_header_Options(
    uint32_t version, const bc_hash_digest_t* previous_block_hash,
    const bc_hash_digest_t* merkle, uint32_t timestamp, uint32_t bits,
    uint32_t nonce);

// Destructor
void bc_destroy_header(const bc_header_t* self);

// Operators
void bc_header__copy(bc_header_t* self, const bc_header_t* other);

bool bc_header__equals(const bc_header_t* self, const bc_header_t* other);
bool bc_header__not_equals(const bc_header_t* self, const bc_header_t* other);

// Deserialization.
//-----------------------------------------------------------------------------
bc_header_t* bc_header__factory_from_data(
    const bc_data_chunk_t* data);

bool bc_header__from_data(
    bc_header_t* self, const bc_data_chunk_t* data);

bool bc_header__is_valid(const bc_header_t* self);

// Serialization.
//-----------------------------------------------------------------------------

bc_data_chunk_t* bc_header__to_data(const bc_header_t* self);

// Properties (size, accessors, cache).
//-----------------------------------------------------------------------------

uint64_t bc_header__satoshi_fixed_size();
uint64_t bc_header__serialized_size(const bc_header_t* self);

// Member variables
uint32_t bc_header__version(const bc_header_t* self);
void bc_header__set_version(bc_header_t* self, uint32_t version);

bc_hash_digest_t* bc_header__previous_block_hash(const bc_header_t* self);
void bc_header__set_previous_block_hash(bc_header_t* self,
    const bc_hash_digest_t* previous_block_hash);

bc_hash_digest_t* bc_header__merkle(const bc_header_t* self);
void bc_header__set_merkle(bc_header_t* self,
    const bc_hash_digest_t* merkle);

uint32_t bc_header__timestamp(const bc_header_t* self);
void bc_header__set_timestamp(bc_header_t* self, uint32_t timestamp);

uint32_t bc_header__bits(const bc_header_t* self);
void bc_header__set_bits(bc_header_t* self, uint32_t bits);

uint32_t bc_header__nonce(const bc_header_t* self);
void bc_header__set_nonce(bc_header_t* self, uint32_t nonce);

// Validation.
//-----------------------------------------------------------------------------

bool bc_header__is_valid_time_stamp(const bc_header_t* self);
bool bc_header__is_valid_proof_of_work(const bc_header_t* self);

bc_error_code_t* bc_header__check(const bc_header_t* self);
bc_error_code_t* bc_header__accept(const bc_header_t* self,
    const bc_chain_state_t* state);

