typedef struct bc_point_iterator_t bc_point_iterator_t;
typedef struct bc_point_indexes_t bc_point_indexes_t;
typedef struct bc_string_t bc_string_t;

typedef struct bc_point_t bc_point_t;
// Static values
/// This is a sentinel used in .index to indicate no output, e.g. coinbase.
/// This value is serialized and defined by consensus, not implementation.
uint32_t bc_point__null_index();
// Static functions
bc_point_t* bc_point__factory_from_data(const bc_data_chunk_t* data);
uint64_t bc_point__satoshi_fixed_size();
// Constructor
bc_point_t* bc_create_point();
// Destructor
void bc_destroy_point(bc_point_t* self);
// Operators
bool bc_point__equals(const bc_point_t* left, const bc_point_t* right);
bool bc_point__not_equals(const bc_point_t* left, const bc_point_t* right);
// Member functions
uint64_t bc_point__checksum(const bc_point_t* self);
bool bc_point__is_null(const bc_point_t* self);
bool bc_point__from_data(bc_point_t* self, const bc_data_chunk_t* data);
bc_data_chunk_t* bc_point__to_data(const bc_point_t* self);
bc_string_t* bc_point__to_string(const bc_point_t* self);
bool bc_point__is_valid(const bc_point_t* self);
void bc_point__reset(bc_point_t* self);
uint64_t bc_point__serialized_size(const bc_point_t* self);
bc_point_iterator_t* bc_point__begin(const bc_point_t* self);
bc_point_iterator_t* bc_point__end(const bc_point_t* self);
// Member variables
bc_hash_digest_t* bc_point__hash(const bc_point_t* self);
void bc_point__set_hash(bc_point_t* self, const bc_hash_digest_t* hash);
uint32_t bc_point__index(const bc_point_t* self);
void bc_point__set_index(bc_point_t* self, uint32_t index);

