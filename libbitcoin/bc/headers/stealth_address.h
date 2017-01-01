typedef struct bc_binary_t bc_binary_t;
typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_ec_compressed_t bc_ec_compressed_t;
typedef struct bc_point_list_t bc_point_list_t;
typedef struct bc_string_t bc_string_t;

typedef struct bc_stealth_address_t bc_stealth_address_t;

/// Static values
uint8_t bc_stealth_address__mainnet_p2kh();
uint8_t bc_stealth_address__reuse_key_flag();
uint8_t bc_stealth_address__max_filter_bits();

/// Constructors.
bc_stealth_address_t* bc_create_stealth_address();
bc_stealth_address_t* bc_create_stealth_address_Data(
    const bc_data_chunk_t* decoded);
bc_stealth_address_t* bc_create_stealth_address_String(const char* encoded);
bc_stealth_address_t* bc_create_stealth_address_copy(
    const bc_stealth_address_t* other);
bc_stealth_address_t* bc_create_stealth_address_Options(
    const bc_binary_t* filter, const bc_ec_compressed_t* scan_key,
    const bc_point_list_t* spend_keys, uint8_t signatures, uint8_t version);

/// Destructor
void bc_destroy_stealth_address(bc_stealth_address_t* self);

/// Operators.
bool bc_stealth_address__less_than(const bc_stealth_address_t* self,
    const bc_stealth_address_t* other);
bool bc_stealth_address__equals(const bc_stealth_address_t* self,
    const bc_stealth_address_t* other);
bool bc_stealth_address__not_equals(const bc_stealth_address_t* self,
    const bc_stealth_address_t* other);
bc_stealth_address_t* bc_stealth_address__copy(
    bc_stealth_address_t* self, const bc_stealth_address_t* other);
// Stream operators ignored.

/// Cast operators.
bool bc_stealth_address__is_valid(const bc_stealth_address_t* self);

/// Serializer.
bc_string_t* bc_stealth_address__encoded(const bc_stealth_address_t* self);

/// Accessors.
uint8_t bc_stealth_address__version(const bc_stealth_address_t* self);
bc_ec_compressed_t* bc_stealth_address__scan_key(
    const bc_stealth_address_t* self);
bc_point_list_t* bc_stealth_address__spend_keys(
    const bc_stealth_address_t* self);
uint8_t bc_stealth_address__signatures(const bc_stealth_address_t* self);
bc_binary_t* bc_stealth_address__filter(const bc_stealth_address_t* self);

/// Methods.
bc_data_chunk_t* bc_stealth_address__to_chunk(
    const bc_stealth_address_t* self);

