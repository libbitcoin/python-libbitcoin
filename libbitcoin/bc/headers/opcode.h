typedef struct bc_string_t bc_string_t;

/// Convert the opcode to a mnemonic string.
bc_string_t* bc_opcode_to_string(bc_opcode_t value, uint32_t active_forks);

/// Convert a string to an opcode.
bool bc_opcode_from_string(bc_opcode_t* out_code, const char* value);

/// Convert any opcode to a string hexadecimal representation.
bc_string_t* bc_opcode_to_hexadecimal(bc_opcode_t code);

/// Convert any hexadecimal byte to an opcode.
bool bc_opcode_from_hexadecimal(bc_opcode_t* out_code, const char* value);

