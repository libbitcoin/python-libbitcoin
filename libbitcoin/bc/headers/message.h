typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_ec_private_t bc_ec_private_t;
typedef struct bc_hash_digest_t bc_hash_digest_t;
typedef struct bc_payment_address_t bc_payment_address_t;

/**
 * A message signature is an EC signature with one prefix byte.
 */
typedef struct bc_message_signature_t bc_message_signature_t;

/**
 * Hashes a messages in preparation for signing.
 */
bc_hash_digest_t* bc_hash_message(const bc_data_chunk_t* message);

/**
 * Signs a message using deterministic signature.
 * @param[in] out_signature The signature in Bitcoin's own format.
 * This should be base64 encoded for presentation to the user.
 * @return true if wif is valid and signature encoding is successful.
 */
bool bc_sign_message(bc_message_signature_t* signature,
    const bc_data_chunk_t* message, const bc_ec_private_t* secret);

/**
 * Signs a message using deterministic signature.
 * @param[in] out_signature The signature in Bitcoin's own format.
 * This should be base64 encoded for presentation to the user.
 * @return true if wif is valid and signature encoding is successful.
 */
bool bc_sign_message_String(bc_message_signature_t* out_signature,
    const bc_data_chunk_t* message, const char* wif);

/**
 * Signs a message using deterministic signature.
 * @param[in] out_signature The signature in Bitcoin's own format.
 * This should be base64 encoded for presentation to the user.
 * @param[in] compressed true if the bitcoin address derived from the
 * private key is in compressed format.
 * @return true if signature encoding is successful.
 */
bool bc_sign_message_Secret(bc_message_signature_t* out_signature,
    const bc_data_chunk_t* message, const bc_ec_secret_t* secret);
bool bc_sign_message_Secret_nocompress(bc_message_signature_t* out_signature,
    const bc_data_chunk_t* message, const bc_ec_secret_t* secret);

/**
 * Verifies a message.
 * @param signature a message signature in Bitcoin's own format.
 * The user will generally provide this as a base64 string,
 * which the user interface must decode.
 * @return false if the signature does not match the address or if there are
 * any errors in the signature encoding.
 */
bool bc_verify_message(const bc_data_chunk_t* message,
    const bc_payment_address_t* address,
    const bc_message_signature_t* signature);

/// Exposed primarily for independent testability.
bool bc_recovery_id_to_magic(uint8_t* out_magic, uint8_t recovery_id,
    bool compressed);

/// Exposed primarily for independent testability.
bool bc_magic_to_recovery_id(uint8_t* out_recovery_id, bool* out_compressed,
    uint8_t magic);

