typedef struct bc_ec_compressed_t bc_ec_compressed_t;
typedef struct bc_ec_uncompressed_t bc_ec_uncompressed_t;
typedef struct bc_ec_private_t bc_ec_private_t;
typedef struct bc_payment_address_t bc_payment_address_t;
typedef struct bc_string_t bc_string_t;

/// Use to pass an ec point as either ec_compressed or ec_uncompressed.
/// ec_public doesn't carry a version for address creation or base58 encoding.
typedef struct bc_ec_public_t bc_ec_public_t;

/// Static values
uint8_t bc_ec_public__compressed_even();
uint8_t bc_ec_public__compressed_odd();
uint8_t bc_ec_public__uncompressed();
uint8_t bc_ec_public__mainnet_p2kh();
/// Constructors.
bc_ec_public_t* bc_create_ec_public();
bc_ec_public_t* bc_create_ec_public_copy(const bc_ec_public_t* other);
bc_ec_public_t* bc_create_ec_public_Private(const bc_ec_private_t* secret);
bc_ec_public_t* bc_create_ec_public_Data(const bc_data_chunk_t* decoded);
bc_ec_public_t* bc_create_ec_public_String(const char* base16);
bc_ec_public_t* bc_create_ec_public_CompPoint(
    const bc_ec_compressed_t* point);
bc_ec_public_t* bc_create_ec_public_CompPoint_nocompress(
    const bc_ec_compressed_t* point);
bc_ec_public_t* bc_create_ec_public_UncompPoint(
    const bc_ec_uncompressed_t* point);
bc_ec_public_t* bc_create_ec_public_UncompPoint_compress(
    const bc_ec_uncompressed_t* point);
/// Destructor
void bc_destroy_ec_public(bc_ec_public_t* self);
/// Operators
bool bc_ec_public__less_than(const bc_ec_public_t* self,
    const bc_ec_public_t* other);
bool bc_ec_public__equals(const bc_ec_public_t* self,
    const bc_ec_public_t* other);
bool bc_ec_public__not_equals(const bc_ec_public_t* self,
    const bc_ec_public_t* other);
void bc_ec_public__copy(bc_ec_public_t* self, const bc_ec_public_t* other);
// Skipping stream operators.
bool bc_ec_public__is_valid(const bc_ec_public_t* self);
/// Serializer.
bc_string_t* bc_ec_public__encoded(const bc_ec_public_t* self);
/// Accessors.
bc_ec_compressed_t* bc_ec_public__point(const bc_ec_public_t* self);
// TODO: these 3 functions are undefined in libbitcoin -----------
//uint16_t bc_ec_public_version(const bc_ec_public_t* self);
//uint8_t bc_ec_public_payment_version(const bc_ec_public_t* self);
//uint8_t bc_ec_public_wif_version(const bc_ec_public_t* self);
// ---------------------------------------------------------------
bool bc_ec_public__compressed(const bc_ec_public_t* self);
/// Methods.
bool bc_ec_public__to_data(const bc_ec_public_t* self, bc_data_chunk_t* out);
bool bc_ec_public__to_uncompressed(
    const bc_ec_public_t* self, bc_ec_uncompressed_t* out);
bc_payment_address_t* bc_ec_public__to_payment_address(
    const bc_ec_public_t* self);
bc_payment_address_t* bc_ec_public__to_payment_address_Version(
    const bc_ec_public_t* self, uint8_t version);

