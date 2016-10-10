/**
 * A valid mnemonic dictionary has exactly this many words.
 */
size_t bc_dictionary_size();

/**
 * A dictionary for creating mnemonics.
 * The bip39 spec calls this a "wordlist".
 * This is a POD type, which means the compiler can write it directly
 * to static memory with no run-time overhead.
 */
typedef struct bc_dictionary_t bc_dictionary_t;
void bc_destroy_dictionary(bc_dictionary_t* self);

// Individual built-in languages:
bc_dictionary_t* bc_dictionary_en();
bc_dictionary_t* bc_dictionary_es();
bc_dictionary_t* bc_dictionary_ja();
bc_dictionary_t* bc_dictionary_zh_Hans();
bc_dictionary_t* bc_dictionary_zh_Hant();

// All built-in languages:
size_t bc_all_dictionaries_size();
bc_dictionary_t* bc_all_dictionaries_get(size_t i);

