typedef struct bc_string_t bc_string_t;

uint8_t bc_btc_decimal_places();
uint8_t bc_mbtc_decimal_places();
uint8_t bc_ubtc_decimal_places();

/**
 * Validates and parses an amount string according to the BIP 21 grammar.
 * @param decmial_places the location of the decimal point.
 * The default is 0, which treats the input as a normal integer.
 * @param strict true to treat fractional results as an error,
 * or false to round them upwards.
 * @return false for failure.
 */
bool bc_decode_base10(uint64_t* out, const char* amount);
bool bc_decode_base10_Places(uint64_t* out, const char* amount,
    uint8_t decimal_places);
bool bc_decode_base10_Places_nostrict(uint64_t* out, const char* amount,
    uint8_t decimal_places);

/**
 * Writes a Bitcoin amount to a string, following the BIP 21 grammar.
 * Avoids the rounding issues often seen with floating-point methods.
 * @param decmial_places the location of the decimal point.
 * The default is 0, which treats the input as a normal integer.
 */
bc_string_t* bc_encode_base10(uint64_t amount);
bc_string_t* bc_encode_base10_Places(uint64_t amount, uint8_t decimal_places);

