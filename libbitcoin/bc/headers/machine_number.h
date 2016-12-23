typedef struct bc_data_chunk_t bc_data_chunk_t;

/**
 * Numeric opcodes (OP_1ADD, etc) are restricted to operating on
 * 4-byte integers. The semantics are subtle, though: operands must be
 * in the range [-2^31 +1...2^31 -1], but results may overflow (and are
 * valid as long as they are not used in a subsequent numeric operation).
 *
 * number enforces those semantics by storing results as
 * an int64 and allowing out-of-range values to be returned as a vector of
 * bytes but throwing an exception if arithmetic is done or the result is
 * interpreted as an integer.
 */
typedef struct bc_machine_number_t bc_machine_number_t;

uint8_t bc_machine_number__negative_1();
uint8_t bc_machine_number__negative_0();
uint8_t bc_machine_number__positive_0();
uint8_t bc_machine_number__positive_1();
uint8_t bc_machine_number__positive_2();
uint8_t bc_machine_number__positive_3();
uint8_t bc_machine_number__positive_4();
uint8_t bc_machine_number__positive_5();
uint8_t bc_machine_number__positive_6();
uint8_t bc_machine_number__positive_7();
uint8_t bc_machine_number__positive_8();
uint8_t bc_machine_number__positive_9();
uint8_t bc_machine_number__positive_10();
uint8_t bc_machine_number__positive_11();
uint8_t bc_machine_number__positive_12();
uint8_t bc_machine_number__positive_13();
uint8_t bc_machine_number__positive_14();
uint8_t bc_machine_number__positive_15();
uint8_t bc_machine_number__positive_16();
uint8_t bc_machine_number__negative_mask();

/// Construct with zero value.
bc_machine_number_t* bc_create_machine_number();

/// Construct with specified value.
bc_machine_number_t* bc_create_machine_number_Value(int64_t value);

// Destructor
void bc_destroy_machine_number(bc_machine_number_t* self);

/// Replace the value derived from a byte vector with LSB first ordering.
bool bc_machine_number__set_data(bc_machine_number_t* self,
    const bc_data_chunk_t* data, size_t max_size);

// Properties
//-----------------------------------------------------------------------------

/// Return the value as a byte vector with LSB first ordering.
bc_data_chunk_t* bc_machine_number__data(const bc_machine_number_t* self);

/// Return the value bounded by the limits of int32.
int32_t bc_machine_number__int32(const bc_machine_number_t* self);

/// Return the unbounded value.
int64_t bc_machine_number__int64(const bc_machine_number_t* self);

// Stack Helpers
//-----------------------------------------------------------------------------

/// Return value as stack boolean (nonzero is true).
bool bc_machine_number__is_true(const bc_machine_number_t* self);

/// Return value as stack boolean (zero is false).
bool bc_machine_number__is_false(const bc_machine_number_t* self);

// Operators
//-----------------------------------------------------------------------------

//************************************************************************
// CONSENSUS: script::number implements consensus critical overflow
// behavior for all operators, specifically [-, +, +=, -=].
//*************************************************************************

bool bc_machine_number__greater_than(
    const bc_machine_number_t* self, int64_t value);
bool bc_machine_number__less_than(
    const bc_machine_number_t* self, int64_t value);
bool bc_machine_number__greater_than_or_equals(
    const bc_machine_number_t* self, int64_t value);
bool bc_machine_number__less_than_or_equals(
    const bc_machine_number_t* self, int64_t value);
bool bc_machine_number__equals(
    const bc_machine_number_t* self, int64_t value);
bool bc_machine_number__not_equals(
    const bc_machine_number_t* self, int64_t value);

bool bc_machine_number__greater_than_Number(
    const bc_machine_number_t* self, const bc_machine_number_t* other);
bool bc_machine_number__less_than_Number(
    const bc_machine_number_t* self, const bc_machine_number_t* other);
bool bc_machine_number__greater_than_or_equals_Number(
    const bc_machine_number_t* self, const bc_machine_number_t* other);
bool bc_machine_number__less_than_or_equals_Number(
    const bc_machine_number_t* self, const bc_machine_number_t* other);
bool bc_machine_number__equals_Number(
    const bc_machine_number_t* self, const bc_machine_number_t* other);
bool bc_machine_number__not_equals_Number(
    const bc_machine_number_t* self, const bc_machine_number_t* other);

bc_machine_number_t* bc_machine_number__positive(
    const bc_machine_number_t* self);
bc_machine_number_t* bc_machine_number__negative(
    const bc_machine_number_t* self);
bc_machine_number_t* bc_machine_number__add(
    const bc_machine_number_t* self, int64_t value);
bc_machine_number_t* bc_machine_number__sub(
    const bc_machine_number_t* self, int64_t value);
bc_machine_number_t* bc_machine_number__add_Number(
    const bc_machine_number_t* self, const bc_machine_number_t* other);
bc_machine_number_t* bc_machine_number__sub_Number(
    const bc_machine_number_t* self, const bc_machine_number_t* other);

void bc_machine_number__plus_equals(
    bc_machine_number_t* self, int64_t value);
void bc_machine_number__minus_equals(
    bc_machine_number_t* self, int64_t value);
void bc_machine_number__plus_equals_Number(
    bc_machine_number_t* self, const bc_machine_number_t* other);
void bc_machine_number__minus_equals_Number(
    bc_machine_number_t* self, const bc_machine_number_t* other);

