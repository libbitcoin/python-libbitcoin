typedef struct bc_binary_t bc_binary_t;
typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_ec_compressed_t bc_ec_compressed_t;
typedef struct bc_ec_secret_t bc_ec_secret_t;
typedef struct bc_hash_digest_t bc_hash_digest_t;
typedef struct bc_script_t bc_script_t;

/// Determine if the script is a null-data script of at least 32 data bytes.
bool bc_is_stealth_script(const bc_script_t* script);

/// Convert a stealth info script to a prefix usable for stealth.
bool bc_to_stealth_prefix(uint32_t* out_prefix, const bc_script_t* script);

/// Create a valid stealth ephemeral private key from the provided seed.
bool bc_create_ephemeral_key(bc_ec_secret_t* out_secret,
    const bc_data_chunk_t* seed);

/// Create a stealth null data script the specified filter prefix.
/// Create an ephemeral secret key generated from the seed.
bool bc_create_stealth_data(bc_script_t* out_null_data,
    bc_ec_secret_t* out_secret, const bc_binary_t* filter,
    const bc_data_chunk_t* seed);

/// Create a stealth null data script the specified filter prefix.
/// Use the ephemeral secret key provided by parameter.
bool bc_create_stealth_script(bc_script_t* out_null_data,
    const bc_ec_secret_t* secret, const bc_binary_t* filter,
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

