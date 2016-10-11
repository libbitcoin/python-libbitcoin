typedef struct bc_string_t bc_string_t;

typedef struct bc_error_code_t bc_error_code_t;
bc_error_code_t* bc_create_error_code(bc_error_t error);
bc_error_code_t* bc_create_error_code_default();
void bc_destroy_error_code(bc_error_code_t* self);
bc_string_t* bc_error_code__message(const bc_error_code_t* self);
bool bc_error_code__is_valid(const bc_error_code_t* self);
bool bc_error_code__equals(const bc_error_code_t* self, bc_error_t ec);

