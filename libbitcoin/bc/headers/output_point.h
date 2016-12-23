typedef struct bc_hash_digest_t bc_hash_digest_t;
typedef struct bc_output_t bc_output_t;
typedef struct bc_point_t bc_point_t;
typedef struct bc_chain_point_list_t bc_chain_point_list_t;

typedef struct bc_output_point_validation_t bc_output_point_validation_t;

void bc_destroy_output_point_validation(bc_output_point_validation_t* self);

size_t bc_output_point_validation__not_specified(
    const bc_output_point_validation_t* self);

bool bc_output_point_validation__spent(
    const bc_output_point_validation_t* self);
void bc_output_point_validation__set_spent(
    bc_output_point_validation_t* self, bool spent);

bool bc_output_point_validation__confirmed(
    const bc_output_point_validation_t* self);
void bc_output_point_validation__set_confirmed(
    bc_output_point_validation_t* self, bool confirmed);

size_t bc_output_point_validation__height(
    const bc_output_point_validation_t* self);
void bc_output_point_validation__set_height(
    bc_output_point_validation_t* self, size_t height);

bc_output_t* bc_output_point_validation__cache(
    const bc_output_point_validation_t* self);

typedef struct bc_output_point_t bc_output_point_t;

/// Constructors
bc_output_point_t* bc_create_output_point();
bc_output_point_t* bc_create_output_point_Point(const bc_point_t* value);
bc_output_point_t* bc_create_output_point_copy(const bc_output_point_t* other);
bc_output_point_t* bc_create_output_point_Tuple(
    const bc_hash_digest_t* hash, uint32_t index);

/// Destructor
void bc_destroy_output_point(bc_output_point_t* self);

/// Operators
bool bc_output_point__copy_Point(const bc_output_point_t* self,
    const bc_point_t* other);
bool bc_output_point__copy(const bc_output_point_t* self,
    const bc_output_point_t* other);

bool bc_output_point__equals(const bc_output_point_t* self,
    const bc_output_point_t* other);
bool bc_output_point__not_equals(const bc_output_point_t* self,
    const bc_output_point_t* other);

// Deserialization.
bc_output_point_t* bc_output_point__factory_from_data(
    const bc_data_chunk_t* data);

bc_point_t* bc_output_point__point_Base(bc_output_point_t* self);

/// False if previous output is not cached.
/// True if the previous output is mature enough to spend from target.
bool bc_output_point__is_mature(const bc_output_point_t* self,
    size_t target_height);

bc_output_point_validation_t* bc_output_point__validation(
    const bc_output_point_t* self);

typedef struct bc_points_info_t bc_points_info_t;
bc_points_info_t* bc_create_points_info();
void bc_destroy_points_info(bc_points_info_t* self);
bc_chain_point_list_t* bc_points_info__points(const bc_points_info_t* self);
void bc_points_info__set_points(bc_points_info_t* self,
    const bc_chain_point_list_t* points);
uint64_t bc_points_info__change(const bc_points_info_t* self);
void bc_points_info__set_change(bc_points_info_t* self, uint64_t change);

typedef struct bc_output_info_t bc_output_info_t;
typedef struct bc_output_info_list_t bc_output_info_list_t;
bc_output_info_t* bc_create_output_info();
void bc_destroy_output_info(bc_output_info_t* self);
bc_output_point_t* bc_output_info__point(const bc_output_info_t* self);
void bc_output_info__set_point(bc_output_info_t* self,
    const bc_output_point_t* point);
uint64_t bc_output_info__value(const bc_output_info_t* self);
void bc_output_info__set_value(bc_output_info_t* self, uint64_t value);

