typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_script_t bc_script_t;
typedef struct bc_string_t bc_string_t;

typedef struct bc_output_t bc_output_t;
// Static values
/// This is a sentinel used in .value to indicate not found in store.
/// This is a sentinel used in cache.value to indicate not populated.
uint64_t bc_output__not_found();
// Static functions
bc_output_t* bc_output__factory_from_data(const bc_data_chunk_t* data);
// Constructor
bc_output_t* bc_create_output();
// Destructor
void bc_destroy_output(bc_output_t* self);
// Member functions
bool bc_output__from_data(bc_output_t* self, const bc_data_chunk_t* data);
bc_data_chunk_t* bc_output__to_data(const bc_output_t* self);
bc_string_t* bc_output__to_string(const bc_output_t* self, uint32_t flags);
bool bc_output__is_valid(const bc_output_t* self);
void bc_output__reset(bc_output_t* self);
uint64_t bc_output__serialized_size(const bc_output_t* self);
size_t bc_output__signature_operations(const bc_output_t* self);
// Member variables
uint64_t bc_output__value(const bc_output_t* self);
void bc_output__set_value(bc_output_t* self, uint64_t value);
bc_script_t* bc_output__script(const bc_output_t* self);
void bc_output__set_script(bc_output_t* self, const bc_script_t* script);

