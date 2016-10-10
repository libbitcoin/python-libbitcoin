/// Determine if code is in the op_n range.
bool bc_within_op_n(bc_opcode_t code);

/// Return the op_n index (i.e. value of n).
uint8_t bc_decode_op_n(bc_opcode_t code);

/// Convert data to an opcode.
bc_opcode_t bc_data_to_opcode(const bc_data_chunk_t* value);

/// Convert a string to an opcode.
bc_opcode_t bc_string_to_opcode(const char* value);

/// Convert an opcode to a string.
bc_string_t* bc_opcode_to_string(bc_opcode_t value, uint32_t flags);

