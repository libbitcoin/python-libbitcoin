typedef struct bc_ec_secret_t bc_ec_secret_t;
typedef struct bc_payment_address_t bc_payment_address_t;
typedef struct bc_string_t bc_string_t;

/// Private keys with public key compression metadata:
typedef struct bc_wif_uncompressed_t bc_wif_uncompressed_t;
typedef struct bc_wif_compressed_t bc_wif_compressed_t;

/// Use to pass an ec secret with compresson and version information.
typedef struct bc_ec_private_t bc_ec_private_t;

/// Static values

// WIF carries a compression flag for payment address generation but
// assumes a mapping to payment address version. This is insufficient
// as a parameterized mapping is required, so we use the same technique as
// with hd keys, merging the two necessary values into one version.
uint8_t bc_ec_private__wif();
uint8_t bc_ec_private__mainnet_p2kh();
uint16_t bc_ec_private__mainnet();
uint16_t bc_ec_private__testnet();
uint8_t bc_ec_private__compressed_sentinel();

/// Static functions
uint8_t bc_ec_private__to_address_prefix(uint16_t version);
uint8_t bc_ec_private__to_wif_prefix(uint16_t version);
// Unfortunately can't use this below to define mainnet (MSVC).
uint8_t bc_ec_private__to_version(uint8_t address, uint8_t wif);

/// Constructors
bc_ec_private_t* bc_create_ec_private();
bc_ec_private_t* bc_create_ec_private_copy(const bc_ec_private_t* other);
bc_ec_private_t* bc_create_ec_private_String(
    const char* wif);
bc_ec_private_t* bc_create_ec_private_String_Version(
    const char* wif, uint8_t version);
bc_ec_private_t* bc_create_ec_private_WifComp(
    const bc_wif_compressed_t* wif);
bc_ec_private_t* bc_create_ec_private_WifComp_Version(
    const bc_wif_compressed_t* wif, uint8_t version);
bc_ec_private_t* bc_create_ec_private_WifUncomp(
    const bc_wif_uncompressed_t* wif);
bc_ec_private_t* bc_create_ec_private_WifUncomp_Version(
    const bc_wif_uncompressed_t* wif, uint8_t version);
/// The version is 16 bits. The most significant byte is the WIF prefix and
/// the least significant byte is the address perfix. 0x8000 by default.
bc_ec_private_t* bc_create_ec_private_Secret(
    const bc_ec_secret_t* secret);
bc_ec_private_t* bc_create_ec_private_Secret_Version(
    const bc_ec_secret_t* secret, uint16_t version);
bc_ec_private_t* bc_create_ec_private_Secret_Version_nocompress(
    const bc_ec_secret_t* secret, uint16_t version);

/// Destructor
void bc_destroy_ec_private(bc_ec_private_t* self);

/// Operators.
bool bc_ec_private__less_than(const bc_ec_private_t* self,
    const bc_ec_private_t* other);
bool bc_ec_private__equals(const bc_ec_private_t* self,
    const bc_ec_private_t* other);
bool bc_ec_private__not_equals(const bc_ec_private_t* self,
    const bc_ec_private_t* other);
void bc_ec_private__copy(bc_ec_private_t* self, const bc_ec_private_t* other);
// Skipping stream operators

/// Cast operators.
bool bc_ec_private__is_valid(const bc_ec_private_t* self);

/// Serializer.
bc_string_t* bc_ec_private__encoded(const bc_ec_private_t* self);

/// Accessors.
bc_ec_secret_t* bc_ec_private__secret(const bc_ec_private_t* self);
uint16_t bc_ec_private__version(const bc_ec_private_t* self);
uint8_t bc_ec_private__payment_version(const bc_ec_private_t* self);
uint8_t bc_ec_private__wif_version(const bc_ec_private_t* self);
bool bc_ec_private__compressed(const bc_ec_private_t* self);

/// Methods.
// TODO: ec_public to_public() const
bc_payment_address_t* bc_ec_private__to_payment_address(
    const bc_ec_private_t* self);

