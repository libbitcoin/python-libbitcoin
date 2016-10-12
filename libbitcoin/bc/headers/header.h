typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_hash_digest_t bc_hash_digest_t;

typedef struct bc_header_t bc_header_t;

// Static functions
bc_header_t* bc_header__factory_from_data(
    const bc_data_chunk_t* data);
bc_header_t* bc_header__factory_from_data_without_transaction_count(
    const bc_data_chunk_t* data);
uint64_t bc_header__satoshi_fixed_size_without_transaction_count();

// Constructor
bc_header_t* bc_create_header();
bc_header_t* bc_create_header_copy(const bc_header_t* other);
bc_header_t* bc_create_header_Options(
    uint32_t version, const bc_hash_digest_t* previous_block_hash,
    const bc_hash_digest_t* merkle, uint32_t timestamp, uint32_t bits,
    uint32_t nonce, uint64_t transaction_count);

// Destructor
void bc_destroy_header(const bc_header_t* self);

// Operators
bool bc_header__equals(const bc_header_t* self, const bc_header_t* other);
bool bc_header__not_equals(const bc_header_t* self, const bc_header_t* other);

// Member functions
bool bc_header__from_data(
    bc_header_t* self, const bc_data_chunk_t* data);
bool bc_header__from_data_without_transaction_count(
    bc_header_t* self, const bc_data_chunk_t* data);
bc_data_chunk_t* bc_header__to_data(const bc_header_t* self);
bc_data_chunk_t* bc_header__to_data_without_transaction_count(
    const bc_header_t* self);
bc_hash_digest_t* bc_header__hash(const bc_header_t* self);
bool bc_header__is_valid(const bc_header_t* self);
void bc_header__reset(bc_header_t* self);
uint64_t bc_header__serialized_size(const bc_header_t* self);
uint64_t bc_header__serialized_size_without_transaction_count(
    const bc_header_t* self);

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

// The longest size (64) of a protocol variable int is deserialized here.
// WHen writing a block the size of the transaction collection is used.
uint32_t bc_header__transaction_count(const bc_header_t* self);
void bc_header__set_transaction_count(bc_header_t* self,
    uint32_t transaction_count);

