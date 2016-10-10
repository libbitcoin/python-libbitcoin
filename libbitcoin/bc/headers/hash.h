typedef struct bc_data_chunk_t bc_data_chunk_t;

// Common bitcoin hash container sizes.
size_t bc_hash_size();
size_t bc_half_hash_size();
size_t bc_quarter_hash_size();
size_t bc_long_hash_size();
size_t bc_short_hash_size();
size_t bc_mini_hash_size();

typedef struct bc_hash_digest_t bc_hash_digest_t;
typedef struct bc_half_hash_t bc_half_hash_t;
typedef struct bc_quarter_hash_t bc_quarter_hash_t;
typedef struct bc_long_hash_t bc_long_hash_t;
typedef struct bc_short_hash_t bc_short_hash_t;
typedef struct bc_mini_hash_t bc_mini_hash_t;

// You must use bc_destroy_hash_digest() to delete the result.
bc_hash_digest_t* bc_null_hash();
bc_half_hash_t* bc_null_half_hash();
bc_quarter_hash_t* bc_null_quarter_hash();
bc_long_hash_t* bc_null_long_hash();
bc_short_hash_t* bc_null_short_hash();
bc_mini_hash_t* bc_null_mini_hash();

/**
 * Generate a ripemd160 hash. This hash function is used in script for
 * op_ripemd160.

 * ripemd160(data)
 */
bc_short_hash_t* bc_ripemd160_hash(const bc_data_chunk_t* data);

/**
 * Generate a sha1 hash. This hash function is used in script for op_sha1.
 *
 * sha1(data)
 */
bc_short_hash_t* bc_sha1_hash(const bc_data_chunk_t* data);

/**
 * Generate a sha256 hash. This hash function is used in mini keys.
 *
 * sha256(data)
 */
bc_hash_digest_t* bc_sha256_hash(const bc_data_chunk_t* data);

/**
 * Generate a sha256 hash. This hash function is used in electrum seed
 * stretching (deprecated).
 *
 * sha256(data)
 */
bc_hash_digest_t* bc_sha256_hash_double(
    const bc_data_chunk_t* first, const bc_data_chunk_t* second);

/**
 * Generate a hmac sha256 hash. This hash function is used in deterministic
 * signing.
 *
 * hmac-sha256(data, key)
 */
bc_hash_digest_t* bc_hmac_sha256_hash(
    const bc_data_chunk_t* data, const bc_data_chunk_t* key);

/**
 * Generate a sha512 hash. This hash function is used in bip32 keys.
 *
 * sha512(data)
 */
bc_long_hash_t* bc_sha512_hash(const bc_data_chunk_t* data);

/**
 * Generate a hmac sha512 hash. This hash function is used in bip32 keys.
 *
 * hmac-sha512(data, key)
 */
bc_long_hash_t* bc_hmac_sha512_hash(
    const bc_data_chunk_t* data, const bc_data_chunk_t* key);

/**
 * Generate a pkcs5 pbkdf2 hmac sha512 hash. This hash function is used in
 * bip39 mnemonics.
 *
 * pkcs5_pbkdf2_hmac_sha512(passphrase, salt, iterations)
 */
bc_long_hash_t* bc_pkcs5_pbkdf2_hmac_sha512(
    const bc_data_chunk_t* passphrase,
    const bc_data_chunk_t* salt, size_t iterations);

/**
 * Generate a typical bitcoin hash. This is the most widely used
 * hash function in Bitcoin.
 *
 * sha256(sha256(data))
 */
bc_hash_digest_t* bc_bitcoin_hash(const bc_data_chunk_t* data);

/**
 * Generate a bitcoin short hash. This hash function is used in a
 * few specific cases where short hashes are desired.
 *
 * ripemd160(sha256(data))
 */
bc_short_hash_t* bc_bitcoin_short_hash(const bc_data_chunk_t* data);

/**
 * Generate a scrypt hash of specified length.
 *
 * scrypt(data, salt, params)
 */
bc_data_chunk_t* bc_scrypt(
    const bc_data_chunk_t* data, const bc_data_chunk_t* salt,
    uint64_t N, uint32_t p, uint32_t r, size_t length);

