typedef struct bc_data_chunk_t bc_data_chunk_t;

size_t bc_max_script_number_size();
size_t bc_cltv_max_script_number_size();

/**
 * Numeric opcodes (OP_1ADD, etc) are restricted to operating on
 * 4-byte integers. The semantics are subtle, though: operands must be
 * in the range [-2^31 +1...2^31 -1], but results may overflow (and are
 * valid as long as they are not used in a subsequent numeric operation).
 *
 * script_number enforces those semantics by storing results as
 * an int64 and allowing out-of-range values to be returned as a vector of
 * bytes but throwing an exception if arithmetic is done or the result is
 * interpreted as an integer.
 */
typedef struct bc_script_number_t bc_script_number_t;

/// Construct with zero value, may call set_data() after.
bc_script_number_t* bc_create_script_number_default();
/// Construct with specified value.
bc_script_number_t* bc_create_script_number(int64_t value);

void bc_destroy_script_number(bc_script_number_t* self);

/// Set the value from a byte vector with LSB first ordering.
bool bc_script_number__set_data(const bc_script_number_t* self,
    const bc_data_chunk_t* data, uint8_t max_size);

/// Return the value as a byte vector with LSB first ordering.
bc_data_chunk_t* bc_script_number__data(const bc_script_number_t* self);

/// Return the value bounded by the limits of int32.
int32_t bc_script_number__int32(const bc_script_number_t* self);

/// Return the value.
int64_t bc_script_number__int64(const bc_script_number_t* self);

// Arithmetic with a number.
bc_script_number_t* bc_script_number__add(
    const bc_script_number_t* self, int64_t value);
bc_script_number_t* bc_script_number__subtract(
    const bc_script_number_t* self, int64_t value);

// Arithmetic with another script_number.
bc_script_number_t* bc_script_number__add_ScriptNumber(
    const bc_script_number_t* self, const bc_script_number_t* other);
bc_script_number_t* bc_script_number__subtract_ScriptNumber(
    const bc_script_number_t* self, const bc_script_number_t* other);

/// Math-negated copy of this script_number (throws on minimum value).
bc_script_number_t* bc_script_number__negate(const bc_script_number_t* self);

// Comparison operators with a number.
bool bc_script_number__equals(
    const bc_script_number_t* self, int64_t value);
bool bc_script_number__not_equals(
    const bc_script_number_t* self, int64_t value);
bool bc_script_number__less_than_or_equals(
    const bc_script_number_t* self, int64_t value);
bool bc_script_number__less_than(
    const bc_script_number_t* self, int64_t value);
bool bc_script_number__greater_than_or_equals(
    const bc_script_number_t* self, int64_t value);
bool bc_script_number__greater_than(
    const bc_script_number_t* self, int64_t value);

// Comparison operators with another script_number.
bool bc_script_number__equals_ScriptNumber(
    const bc_script_number_t* self, const bc_script_number_t* other);
bool bc_script_number__not_equals_ScriptNumber(
    const bc_script_number_t* self, const bc_script_number_t* other);
bool bc_script_number__less_than_or_equals_ScriptNumber(
    const bc_script_number_t* self, const bc_script_number_t* other);
bool bc_script_number__less_than_ScriptNumber(
    const bc_script_number_t* self, const bc_script_number_t* other);
bool bc_script_number__greater_than_or_equals_ScriptNumber(
    const bc_script_number_t* self, const bc_script_number_t* other);
bool bc_script_number__greater_than_ScriptNumber(
    const bc_script_number_t* self, const bc_script_number_t* other);

