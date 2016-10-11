/**
 * The secret for aes256 block cypher.
 */
uint8_t bc_aes256_key_size();
typedef struct bc_aes_secret_t bc_aes_secret_t;

/**
 * The data block for use with aes256 block cypher.
 */
uint8_t bc_aes256_block_size();
typedef struct bc_aes_block_t bc_aes_block_t;

/**
 * Perform aes256 encryption on the specified data block.
 */
void bc_aes256_encrypt(const bc_aes_secret_t* key, bc_aes_block_t* block);

/**
 * Perform aes256 decryption on the specified data block.
 */
void bc_aes256_decrypt(const bc_aes_secret_t* key, bc_aes_block_t* block);

