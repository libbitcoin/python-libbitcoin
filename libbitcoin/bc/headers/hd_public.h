typedef struct bc_string_t bc_string_t;
typedef struct bc_ec_compressed_t bc_ec_compressed_t;

uint32_t bc_hd_first_hardened_key();

/// An hd key chain code.
size_t bc_hd_chain_code_size();
typedef struct bc_hd_chain_code_t bc_hd_chain_code_t;
void bc_destroy_hd_chain_code(bc_hd_chain_code_t* self);

/// A decoded hd public or private key.
size_t bc_hd_key_size();
typedef struct bc_hd_key_t bc_hd_key_t;
void bc_destroy_hd_key(bc_hd_key_t* self);

/// Key derivation information used in the serialization format.
typedef struct bc_hd_lineage_t bc_hd_lineage_t;
// prefixes
uint64_t bc_hd_lineage__get_prefixes(bc_hd_lineage_t* self);
void bc_hd_lineage__set_prefixes(
    bc_hd_lineage_t* self, uint64_t prefixes);
// depth
uint8_t bc_hd_lineage__get_depth(bc_hd_lineage_t* self);
void bc_hd_lineage__set_depth(
    bc_hd_lineage_t* self, uint8_t depth);
// parent_fingerprint
uint32_t bc_hd_lineage__get_parent_fingerprint(bc_hd_lineage_t* self);
void bc_hd_lineage__set_parent_fingerprint(
    bc_hd_lineage_t* self,uint32_t parent_fingerprint);
// child_number
uint32_t bc_hd_lineage__get_child_number(bc_hd_lineage_t* self);
void bc_hd_lineage__set_child_number(
    bc_hd_lineage_t* self, uint32_t child_number);
// Comparison operators
bool bc_hd_lineage__equals(bc_hd_lineage_t* a, bc_hd_lineage_t* b);
bool bc_hd_lineage__not_equals(bc_hd_lineage_t* a, bc_hd_lineage_t* b);

/// An extended public key, as defined by BIP 32.
typedef struct bc_hd_public_t bc_hd_public_t;
uint32_t bc_hd_public__mainnet();
uint32_t bc_hd_public__to_prefix(uint64_t prefixes);
/// Constructors.
// hd_public();
bc_hd_public_t* bc_create_hd_public();
// hd_public(const hd_public& other);
bc_hd_public_t* bc_create_hd_public_copy(const bc_hd_public_t* other);
// hd_public(const hd_key& public_key);
bc_hd_public_t* bc_create_hd_public_Key(bc_hd_key_t* public_key);
// hd_public(const hd_key& public_key, uint32_t prefix);
bc_hd_public_t* bc_create_hd_public_Key_Prefix(
    bc_hd_key_t* public_key, uint32_t prefix);
// hd_public(const std::string& encoded);
bc_hd_public_t* bc_create_hd_public_String(const char* encoded);
// hd_public(const std::string& encoded, uint32_t prefix);
bc_hd_public_t* bc_create_hd_public_String_Prefix(
    const char* encoded, uint32_t prefix);
/// Destructor
void bc_destroy_hd_public(bc_hd_public_t* self);
/// Operators.
bool bc_hd_public__less_than(
    const bc_hd_public_t* self, const bc_hd_public_t* other);
bool bc_hd_public__equals(
    const bc_hd_public_t* self, const bc_hd_public_t* other);
bool bc_hd_public__not_equals(
    const bc_hd_public_t* self, const bc_hd_public_t* other);
bc_hd_public_t* bc_hd_public__copy(
    bc_hd_public_t* self, const bc_hd_public_t* other);
// Ignored:
//  friend std::istream& operator>>(std::istream& in, hd_public& to);
//  friend std::ostream& operator<<(std::ostream& out, const hd_public& of);
bool bc_hd_public__is_valid(const bc_hd_public_t* self);
/// Serializer.
bc_string_t* bc_hd_public__encoded(const bc_hd_public_t* self);
/// Accessors.
bc_hd_chain_code_t* bc_hd_public__chain_code(const bc_hd_public_t* self);
bc_hd_lineage_t* bc_hd_public__lineage(const bc_hd_public_t* self);
bc_ec_compressed_t* bc_hd_public__point(const bc_hd_public_t* self);
/// Methods.
bc_hd_key_t* bc_hd_public__to_hd_key(const bc_hd_public_t* self);
bc_hd_public_t* bc_hd_public__derive_public(
    const bc_hd_public_t* self, uint32_t index);

