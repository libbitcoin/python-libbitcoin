typedef struct bc_data_chunk_t bc_data_chunk_t;
bc_data_chunk_t* bc_create_data_chunk();
bc_data_chunk_t* bc_create_data_chunk_copy(const bc_data_chunk_t* other);
bc_data_chunk_t* bc_create_data_chunk_Array(const uint8_t* data, size_t size);
void bc_destroy_data_chunk(bc_data_chunk_t* self);
size_t bc_data_chunk__size(const bc_data_chunk_t* self);
bool bc_data_chunk__empty(const bc_data_chunk_t* self);
void bc_data_chunk__resize(bc_data_chunk_t* self, size_t count);
uint8_t* bc_data_chunk__data(bc_data_chunk_t* self);
void bc_data_chunk__extend_data(
    bc_data_chunk_t* self, const bc_data_chunk_t* other);
bool bc_data_chunk__equals(
    const bc_data_chunk_t* self, const bc_data_chunk_t* other);

