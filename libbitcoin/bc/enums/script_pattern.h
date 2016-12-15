/// Script patterms.
/// Comments from: bitcoin.org/en/developer-guide#signature-hash-types
typedef enum bc_script_pattern_t
{
    /// Null Data
    /// Pubkey Script: OP_RETURN <0 to 80 bytes of data> (formerly 40 bytes)
    /// Null data scripts cannot be spent, so there's no signature script.
    bc_script_pattern__null_data,

    /// Pay to Multisig [BIP11]
    /// Pubkey script: <m> <A pubkey>[B pubkey][C pubkey...] <n> OP_CHECKMULTISIG
    /// Signature script: OP_0 <A sig>[B sig][C sig...]
    bc_script_pattern__pay_multisig,

    /// Pay to Public Key (obsolete)
    bc_script_pattern__pay_public_key,

    /// Pay to Public Key Hash [P2PKH]
    /// Pubkey script: OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
    /// Signature script: <sig> <pubkey>
    bc_script_pattern__pay_key_hash,

    /// Pay to Script Hash [P2SH/BIP16]
    /// The redeem script may be any pay type, but only multisig makes sense.
    /// Pubkey script: OP_HASH160 <Hash160(redeemScript)> OP_EQUAL
    /// Signature script: <sig>[sig][sig...] <redeemScript>
    bc_script_pattern__pay_script_hash,

    /// Sign Multisig script [BIP11]
    bc_script_pattern__sign_multisig,

    /// Sign Public Key (obsolete)
    bc_script_pattern__sign_public_key,

    /// Sign Public Key Hash [P2PKH]
    bc_script_pattern__sign_key_hash,

    /// Sign Script Hash [P2SH/BIP16]
    bc_script_pattern__sign_script_hash,

    /// The script is valid but does not conform to the standard tempaltes.
    /// Such scripts are always accepted if they are mined into blocks, but
    /// transactions with non-standard scripts may not be forwarded by peers.
    bc_script_pattern__non_standard

} bc_script_pattern_t;

