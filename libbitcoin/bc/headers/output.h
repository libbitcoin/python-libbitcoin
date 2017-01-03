typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_payment_address_t bc_payment_address_t;
typedef struct bc_script_t bc_script_t;
typedef struct bc_string_t bc_string_t;

typedef struct bc_output_t bc_output_t;

// Static values
/// This is a sentinel used in .value to indicate not found in store.
/// This is a sentinel used in cache.value to indicate not populated.
/// This is a consensus value used in script::generate_signature_hash.
uint64_t bc_output__not_found();
// Constructor
bc_output_t* bc_create_output();
bc_output_t* bc_create_output_copy(const bc_output_t* other);
bc_output_t* bc_create_output_Value(uint64_t value, const bc_script_t* script);
// Destructor
void bc_destroy_output(bc_output_t* self);

// Operators
void bc_output__copy(bc_output_t* self, const bc_output_t* other);
bool bc_output__equals(const bc_output_t* self, const bc_output_t* other);
bool bc_output__not_equals(const bc_output_t* self, const bc_output_t* other);

// Member functions
bc_output_t* bc_output__factory_from_data(const bc_data_chunk_t* data);
bc_output_t* bc_output__factory_from_data_nowire(const bc_data_chunk_t* data);
bool bc_output__from_data(bc_output_t* self, const bc_data_chunk_t* data);
bool bc_output__from_data_nowire(bc_output_t* self, const bc_data_chunk_t* data);

bool bc_output__is_valid(const bc_output_t* self);

bc_data_chunk_t* bc_output__to_data(const bc_output_t* self);
bc_data_chunk_t* bc_output__to_data_nowire(const bc_output_t* self);

size_t bc_output__serialized_size(const bc_output_t* self);
size_t bc_output__serialized_size_nowire(const bc_output_t* self);

uint64_t bc_output__value(const bc_output_t* self);
void bc_output__set_value(bc_output_t* self, uint64_t value);

bc_script_t* bc_output__script(const bc_output_t* self);
void bc_output__set_script(bc_output_t* self, const bc_script_t* script);

/// The payment address extracted from this output as a standard script.
bc_payment_address_t* bc_output__address(const bc_output_t* self);

size_t bc_output__signature_operations(const bc_output_t* self);

