typedef struct bc_data_chunk_t bc_data_chunk_t;
typedef struct bc_dictionary_t bc_dictionary_t;
typedef struct bc_long_hash_t bc_long_hash_t;
typedef struct bc_string_list_t bc_string_list_t;

/**
 * A valid mnemonic word count is evenly divisible by this number.
 */
size_t bc_mnemonic_word_multiple();

/**
 * A valid seed byte count is evenly divisible by this number.
 */
size_t bc_mnemonic_seed_multiple();

/**
 * Represents a mnemonic word list.
 */
typedef struct bc_string_list_t bc_word_list_t;

/**
 * Create a new mnenomic (list of words) from provided entropy and a dictionary
 * selection. The mnemonic can later be converted to a seed for use in wallet
 * creation. Entropy byte count must be evenly divisible by 4.
 */
bc_word_list_t* bc_create_mnemonic(const bc_data_chunk_t* entropy);
bc_word_list_t* bc_create_mnemonic_Dict(const bc_data_chunk_t* entropy,
    const bc_dictionary_t* lexicon);

/**
 * Checks a mnemonic against a dictionary to determine if the
 * words are spelled correctly and the checksum matches.
 * The words must have been created using mnemonic encoding.
 */
bool bc_validate_mnemonic(const bc_word_list_t* mnemonic,
    const bc_dictionary_t* lexicon);

/**
 * Checks that a mnemonic is valid in at least one of the provided languages.
 */
bool bc_validate_mnemonic_all_languages(const bc_word_list_t* mnemonic);

/**
 * Convert a mnemonic with no passphrase to a wallet-generation seed.
 */
bc_long_hash_t* bc_decode_mnemonic(const bc_word_list_t* mnemonic);

