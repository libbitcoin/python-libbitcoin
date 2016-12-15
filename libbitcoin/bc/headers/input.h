typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_output_point_t bc_output_point_t;
typedef struct bc_script_t bc_script_t;
typedef struct bc_string_t bc_string_t;

typedef struct bc_input_t bc_input_t;

// Constructor
bc_input_t* bc_create_input();
bc_input_t* bc_create_input_copy(const bc_input_t* other);
bc_input_t* bc_create_input_Values(
    const bc_output_point_t* previous_output, const bc_script_t* script,
    uint32_t sequence);
// Destructor
void bc_destroy_input(bc_input_t* self);
// Operators
void bc_input__copy(bc_input_t* self, const bc_input_t* other);
bool bc_input__equals(bc_input_t* self, const bc_input_t* other);
bool bc_input__not_equals(bc_input_t* self, const bc_input_t* other);

// Deserialization.
bc_input_t* bc_input__factory_from_data(const bc_data_chunk_t* data);
bc_input_t* bc_input__factory_from_data_nowire(const bc_data_chunk_t* data);

bool bc_input__from_data(bc_input_t* self, const bc_data_chunk_t* data);
bool bc_input__from_data_nowire(bc_input_t* self, const bc_data_chunk_t* data);

bool bc_input__is_valid(const bc_input_t* self);

// Serialization.
bc_data_chunk_t* bc_input__to_data(const bc_input_t* self);
bc_data_chunk_t* bc_input__to_data_nowire(const bc_input_t* self);

// Properties
uint64_t bc_input__serialized_size(const bc_input_t* self);
uint64_t bc_input__serialized_size_nowire(const bc_input_t* self);

bc_output_point_t* bc_input__previous_output(const bc_input_t* self);
void bc_input__set_previous_output(bc_input_t* self,
    bc_output_point_t* previous_output);

bc_script_t* bc_input__script(const bc_input_t* self);
void bc_input__set_script(bc_input_t* self, const bc_script_t* script);

uint32_t bc_input__sequence(const bc_input_t* self);
void bc_input__set_sequence(bc_input_t* self, uint32_t sequence);

bool bc_input__is_final(const bc_input_t* self);
size_t bc_input__signature_operations(
    const bc_input_t* self, bool bip16_active);

