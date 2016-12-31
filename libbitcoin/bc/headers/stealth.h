typedef struct bc_binary_t bc_binary_t;
typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_ec_compressed_t bc_ec_compressed_t;
typedef struct bc_ec_secret_t bc_ec_secret_t;
typedef struct bc_hash_digest_t bc_hash_digest_t;
typedef struct bc_script_t bc_script_t;

uint8_t bc_ephemeral_public_key_sign();

/// Determine if the script is a null-data script of at least 32 data bytes.
bool bc_is_stealth_script(const bc_script_t* script);

/// Convert a stealth info script to a prefix usable for stealth.
bool bc_to_stealth_prefix(uint32_t* out_prefix, const bc_script_t* script);

/// Create a valid stealth ephemeral private key from the provided seed.
bool bc_create_ephemeral_key(bc_ec_secret_t* out_secret,
    const bc_data_chunk_t* seed);

/// Create an ephemeral public key from the provided seed with the
/// null-data script data value that produces the desired filter prefix.
bool bc_create_stealth_data(bc_data_chunk_t* out_stealth_data,
    bc_ec_secret_t* out_secret, const bc_binary_t* filter,
    const bc_data_chunk_t* seed);

/// Extract the stealth ephemeral public key from an output script.
bool bc_extract_ephemeral_key(
    bc_ec_compressed_t* out_ephemeral_public_key, const bc_script_t* script);

/// Extract the unsigned stealth ephemeral public key from an output script.
bool bc_extract_ephemeral_key_Hash(
    bc_hash_digest_t* out_unsigned_ephemeral_key, const bc_script_t* script);

/// Calculate the shared secret.
bool bc_shared_secret(bc_ec_secret_t* out_shared, const bc_ec_secret_t* secret,
    const bc_ec_compressed_t* point);

/// Uncover the stealth public key.
bool bc_uncover_stealth_Public(bc_ec_compressed_t* out_stealth,
    const bc_ec_compressed_t* ephemeral_or_scan,
    const bc_ec_secret_t* scan_or_ephemeral,
    const bc_ec_compressed_t* spend);

/// Uncover the stealth secret.
bool bc_uncover_stealth_Secret(bc_ec_secret_t* out_stealth,
    const bc_ec_compressed_t* ephemeral_or_scan,
    const bc_ec_secret_t* scan_or_ephemeral,
    const bc_ec_secret_t* spend);

