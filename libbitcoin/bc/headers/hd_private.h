typedef struct bc_ec_secret_t bc_ec_secret_t;
typedef struct bc_hd_key_t bc_hd_key_t;
typedef struct bc_hd_public_t bc_hd_public_t;
typedef struct bc_string_t bc_string_t;

typedef struct bc_hd_private_t bc_hd_private_t;
uint64_t bc_hd_private__mainnet();
uint64_t bc_hd_private__testnet();
uint32_t bc_hd_private__to_prefix(uint64_t prefixes);
uint64_t bc_hd_private__to_prefixes(
    uint32_t private_prefix, uint32_t public_prefix);
/// Constructors.
bc_hd_private_t* bc_create_hd_private();
bc_hd_private_t* bc_create_hd_private_copy(const bc_hd_private_t* other);
bc_hd_private_t* bc_create_hd_private_Seed(
    const bc_data_chunk_t* seed, uint64_t prefixes);
bc_hd_private_t* bc_create_hd_private_Key(
    const bc_hd_key_t* key);
bc_hd_private_t* bc_create_hd_private_Key_Prefixes(
    const bc_hd_key_t* key, uint64_t prefixes);
bc_hd_private_t* bc_create_hd_private_Key_Prefix(
    const bc_hd_key_t* key, uint32_t public_prefix);
bc_hd_private_t* bc_create_hd_private_String(
    const char* encoded);
bc_hd_private_t* bc_create_hd_private_String_Prefixes(
    const char* encoded, uint64_t prefixes);
bc_hd_private_t* bc_create_hd_private_String_Prefix(
    const char* encoded, uint32_t public_prefix);
void bc_destroy_hd_private(bc_hd_private_t* self);
/// Operators.
bool bc_hd_private__less_than(
    bc_hd_private_t* self, const bc_hd_private_t* other);
bool bc_hd_private__equals(
    bc_hd_private_t* self, const bc_hd_private_t* other);
bool bc_hd_private__not_equals(
    bc_hd_private_t* self, const bc_hd_private_t* other);
bc_hd_public_t* bc_hd_private__hd_public_Base(bc_hd_private_t* self);
// Simply returns itself again
bc_hd_private_t* bc_hd_private__copy(
    bc_hd_private_t* self, const bc_hd_private_t* other);
// istream and ostream operators ignored.
/// Serializer.
bc_string_t* bc_hd_private__encoded(const bc_hd_private_t* self);
/// Accessors.
bc_ec_secret_t* bc_hd_private__secret(const bc_hd_private_t* self);
/// Methods.
bc_hd_key_t* bc_hd_private__to_hd_key(const bc_hd_private_t* self);
bc_hd_public_t* bc_hd_private__to_public(const bc_hd_private_t* self);
bc_hd_private_t* bc_hd_private__derive_private(
    const bc_hd_private_t* self, uint32_t index);
bc_hd_public_t* bc_hd_private__derive_public(
    const bc_hd_private_t* self, uint32_t index);

