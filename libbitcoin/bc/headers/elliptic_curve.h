typedef struct bc_ec_secret_t bc_ec_secret_t;
typedef struct bc_ec_compressed_t bc_ec_compressed_t;
typedef struct bc_ec_uncompressed_t bc_ec_uncompressed_t;
typedef struct bc_ec_signature_t bc_ec_signature_t;

typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_hash_digest_t bc_hash_digest_t;

// DER encoded signature:
size_t bc_max_der_signature_size();
// This type is actually a data_chunk typedef
typedef struct bc_data_chunk_t bc_der_signature_t;

/// DER encoded signature with sighash byte for input endorsement:
size_t bc_max_endorsement_size();
// This type is actually a data_chunk typedef
typedef struct bc_data_chunk_t bc_endorsement_t;

/// Recoverable ecdsa signature for message signing:
typedef struct bc_recoverable_signature_t bc_recoverable_signature_t;
bc_recoverable_signature_t* bc_create_recoverable_signature();
void bc_destroy_recoverable_signature(bc_recoverable_signature_t* self);
bc_ec_signature_t* bc_recoverable_signature__signature(
    const bc_recoverable_signature_t* self);
void bc_recoverable_signature__set_signature(
    bc_recoverable_signature_t* self, const bc_ec_signature_t* signature);
uint8_t bc_recoverable_signature__recovery_id(
    const bc_recoverable_signature_t* self);
void bc_recoverable_signature__set_recovery_id(
    const bc_recoverable_signature_t* self, uint8_t recovery_id);

bc_ec_compressed_t* null_compressed_point();
bc_ec_uncompressed_t* null_uncompressed_point();

// Add and multiply EC values
// ----------------------------------------------------------------------------

/// Compute the sum a += G*b, where G is the curve's generator point.
/// return false on failure (such as infinity or zero).
bool bc_ec_add_compressed(
    bc_ec_compressed_t* point, const bc_ec_secret_t* secret);

/// Compute the sum a += G*b, where G is the curve's generator point.
/// return false on failure (such as infinity or zero).
bool bc_ec_add_uncompressed(
    bc_ec_uncompressed_t* point, const bc_ec_secret_t* secret);

/// Compute the sum a = (a + b) % n, where n is the curve order.
/// return false on failure (such as a zero result).
bool bc_ec_add(bc_ec_secret_t* left, const bc_ec_secret_t* right);

/// Compute the product point *= secret.
/// return false on failure (such as infinity or zero).
bool bc_ec_multiply_compressed(
    bc_ec_compressed_t* point, const bc_ec_secret_t* secret);

/// Compute the product point *= secret.
/// return false on failure (such as infinity or zero).
bool bc_ec_multiply_uncompressed(
    bc_ec_uncompressed_t* point, const bc_ec_secret_t* secret);

/// Compute the product a = (a * b) % n, where n is the curve order.
/// return false on failure (such as a zero result).
bool bc_ec_multiply(bc_ec_secret_t* left, const bc_ec_secret_t* right);

// Convert keys
// ----------------------------------------------------------------------------

/// Convert an uncompressed public point to compressed.
bool bc_compress(bc_ec_compressed_t* out, const bc_ec_uncompressed_t* point);

/// Convert a compressed public point to decompressed.
bool bc_decompress(bc_ec_uncompressed_t* out, const bc_ec_compressed_t* point);

/// Convert a secret to a compressed public point.
bool bc_secret_to_public_compressed(
    bc_ec_compressed_t* out, const bc_ec_secret_t* secret);

/// Convert a secret parameter to an uncompressed public point.
bool bc_secret_to_public_uncompressed(
    bc_ec_uncompressed_t* out, const bc_ec_secret_t* secret);

// Verify keys
// ----------------------------------------------------------------------------

/// Verify a secret.
bool bc_verify_secret(const bc_ec_secret_t* secret);

/// Verify a point.
bool bc_verify_compressed(const bc_ec_compressed_t* point);

/// Verify a point.
bool bc_verify_uncompressed(const bc_ec_uncompressed_t* point);

// Detect public keys
// ----------------------------------------------------------------------------

/// Fast detection of compressed public key structure.
bool bc_is_compressed_key(const bc_data_chunk_t* point);

/// Fast detection of uncompressed public key structure.
bool bc_is_uncompressed_key(const bc_data_chunk_t* point);

/// Fast detection of compressed or uncompressed public key structure.
bool bc_is_public_key(const bc_data_chunk_t* point);

// DER parse/encode
// ----------------------------------------------------------------------------

/// Parse a DER encoded signature with optional strict DER enforcement.
/// Treat an empty DER signature as invalid, in accordance with BIP66.
bool bc_parse_signature(bc_ec_signature_t* out,
    const bc_der_signature_t* der_signature, bool strict);

/// Encode an EC signature as DER (strict).
bool bc_encode_signature(bc_der_signature_t* out,
    const bc_ec_signature_t* signature);

// EC sign/verify
// ----------------------------------------------------------------------------

/// Create a deterministic ECDSA signature using a private key.
bool bc_sign(bc_ec_signature_t* out, const bc_ec_secret_t* secret,
    const bc_hash_digest_t* hash);

/// Verify an EC signature using a compressed point.
bool bc_verify_signature_compressed(const bc_ec_compressed_t* point,
    const bc_hash_digest_t* hash, const bc_ec_signature_t* signature);

/// Verify an EC signature using an uncompressed point.
bool bc_verify_signature_uncompressed(const bc_ec_uncompressed_t* point,
    const bc_hash_digest_t* hash, const bc_ec_signature_t* signature);

/// Verify an EC signature using a potential point.
bool bc_verify_signature_point(const bc_data_chunk_t* point,
    const bc_hash_digest_t* hash, const bc_ec_signature_t* signature);

// Recoverable sign/recover
// ----------------------------------------------------------------------------

/// Create a recoverable signature for use in message signing.
bool sign_recoverable(bc_recoverable_signature_t* out,
    const bc_ec_secret_t* secret, const bc_hash_digest_t* hash);

/// Recover the compressed point from a recoverable message signature.
bool recover_public_compressed(bc_ec_compressed_t* out,
    const bc_recoverable_signature_t* recoverable,
    const bc_hash_digest_t* hash);

/// Recover the uncompressed point from a recoverable message signature.
bool recover_public_uncompressed(bc_ec_uncompressed_t* out,
    const bc_recoverable_signature_t* recoverable,
    const bc_hash_digest_t* hash);

