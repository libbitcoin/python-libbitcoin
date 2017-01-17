/// Signature hash types.
/// Comments from: bitcoin.org/en/developer-guide#standard-transactions
typedef enum bc_sighash_algorithm_t
{
    /// The default, signs all the inputs and outputs, protecting everything
    /// except the signature scripts against modification.
    bc_sighash_algorithm__all = 0x01,

    /// Signs all of the inputs but none of the outputs, allowing anyone to
    /// change where the satoshis are going unless other signatures using 
    /// other signature hash flags protect the outputs.
    bc_sighash_algorithm__none = 0x02,

    /// The only output signed is the one corresponding to this input (the
    /// output with the same output index number as this input), ensuring
    /// nobody can change your part of the transaction but allowing other 
    /// signers to change their part of the transaction. The corresponding 
    /// output must exist or the value '1' will be signed, breaking the
    /// security scheme. This input, as well as other inputs, are included
    /// in the signature. The sequence numbers of other inputs are not
    /// included in the signature, and can be updated.
    bc_sighash_algorithm__single = 0x03,

    /// The above types can be modified with this flag, creating three new
    /// combined types.
    bc_sighash_algorithm__anyone_can_pay = 0x80,

    /// Signs all of the outputs but only this one input, and it also allows
    /// anyone to add or remove other inputs, so anyone can contribute
    /// additional satoshis but they cannot change how many satoshis are
    /// sent nor where they go.
    bc_sighash_algorithm__all_anyone_can_pay = 0x81,

    /// Signs only this one input and allows anyone to add or remove other
    /// inputs or outputs, so anyone who gets a copy of this input can spend
    /// it however they'd like.
    bc_sighash_algorithm__none_anyone_can_pay = 0x82,

    /// Signs this one input and its corresponding output. Allows anyone to
    /// add or remove other inputs.
    bc_sighash_algorithm__single_anyone_can_pay = 0x83,

} bc_sighash_algorithm_t;

