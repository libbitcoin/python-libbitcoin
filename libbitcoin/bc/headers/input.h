typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_output_point_t bc_output_point_t;
typedef struct bc_script_t bc_script_t;
typedef struct bc_string_t bc_string_t;

typedef struct bc_input_t bc_input_t;
// Static functions
bc_input_t* bc_input__factory_from_data(const bc_data_chunk_t* data);
// Constructor
bc_input_t* bc_create_input();
// Destructor
void bc_destroy_input(bc_input_t* self);
// Member functions
bool bc_input__from_data(bc_input_t* self, const bc_data_chunk_t* data);
bc_data_chunk_t* bc_input__to_data(const bc_input_t* self);
bc_string_t* bc_input__to_string(const bc_input_t* self, uint32_t flags);
bool bc_input__is_valid(const bc_input_t* self);
bool bc_input__is_final(const bc_input_t* self);
bool bc_input__is_output_mature(const bc_input_t* self, size_t target_height);
void bc_input__reset(bc_input_t* self);
uint64_t bc_input__serialized_size(const bc_input_t* self);
size_t bc_input__signature_operations(
    const bc_input_t* self, bool bip16_active);
// Member variables
bc_output_point_t* bc_input__previous_output(const bc_input_t* self);
void bc_input__set_previous_output(bc_input_t* self,
    bc_output_point_t* previous_output);
bc_script_t* bc_input__script(const bc_input_t* self);
void bc_input__set_script(bc_input_t* self, const bc_script_t* script);
uint32_t bc_input__sequence(const bc_input_t* self);
void bc_input__set_sequence(bc_input_t* self, uint32_t sequence);

