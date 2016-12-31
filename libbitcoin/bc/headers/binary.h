typedef struct bc_binary_t bc_binary_t;
typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_string_t bc_string_t;

/// Static values
size_t bc_binary__bits_per_block();

/// Static methods
size_t bc_binary__blocks_size(size_t bit_size);
bool bc_binary__is_base2(const char* text);

/// Constructors.
bc_binary_t* bc_create_binary();
bc_binary_t* bc_create_binary_copy(const bc_binary_t* other);
bc_binary_t* bc_create_binary_String(const char* bit_string);
bc_binary_t* bc_create_binary_Blocks(size_t size, const uint8_t* blocks);

/// Destructor
void bc_destroy_binary(bc_binary_t* self);

/// Methods
size_t bc_binary__resize(bc_binary_t* self, size_t size);
bool bc_binary__at(const bc_binary_t* self, size_t index);
bc_data_chunk_t* bc_binary__blocks(const bc_binary_t* self);
bc_string_t* bc_binary__encoded(const bc_binary_t* self);

// size in bits
size_t bc_binary__size(const bc_binary_t* self);
void bc_binary__append(bc_binary_t* self, const bc_binary_t* post);
void bc_binary__prepend(bc_binary_t* self, const bc_binary_t* prior);
void bc_binary__shift_left(bc_binary_t* self, size_t distance);
void bc_binary__shift_right(bc_binary_t* self, size_t distance);
bc_binary_t* bc_binary__substring(bc_binary_t* self, size_t first);
bc_binary_t* bc_binary__substring_Length(bc_binary_t* self,
    size_t first, size_t length);

bool bc_binary__is_prefix_of(const bc_binary_t* self,
    const uint8_t* field_begin, const uint8_t* field_end);
bool bc_binary__is_prefix_of_Uint32(const bc_binary_t* self, uint32_t field);
bool bc_binary__is_prefix_of_Binary(const bc_binary_t* self,
    const bc_binary_t* field);

/// Operators.
bool bc_binary__less_than(const bc_binary_t* self, const bc_binary_t* other);
bool bc_binary__equals(const bc_binary_t* self, const bc_binary_t* other);
bool bc_binary__not_equals(const bc_binary_t* self, const bc_binary_t* other);
void bc_binary__copy(bc_binary_t* self, const bc_binary_t* other);
// Stream operators ignored.

