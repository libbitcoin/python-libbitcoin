typedef struct bc_string_t bc_string_t;
bc_string_t* bc_create_string_default();
bc_string_t* bc_create_string_Length(const char* data, size_t length);
void bc_destroy_string(bc_string_t* self);
const char* bc_string__data(const bc_string_t* self);
bool bc_string__empty(const bc_string_t* self);
size_t bc_string__length(const bc_string_t* self);
bool bc_string__equals(const bc_string_t* self, const bc_string_t* other);
bool bc_string__equals_cstr(const bc_string_t* self, const char* other);

