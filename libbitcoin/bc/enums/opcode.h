typedef enum bc_opcode_t
{
    bc_opcode__zero = 0,
    bc_opcode__special = 1,
    bc_opcode__pushdata1 = 76,
    bc_opcode__pushdata2 = 77,
    bc_opcode__pushdata4 = 78,
    bc_opcode__negative_1 = 79,
    bc_opcode__reserved = 80,  // does nothing
    bc_opcode__op_1 = 81,
    bc_opcode__op_2 = 82,
    bc_opcode__op_3 = 83,
    bc_opcode__op_4 = 84,
    bc_opcode__op_5 = 85,
    bc_opcode__op_6 = 86,
    bc_opcode__op_7 = 87,
    bc_opcode__op_8 = 88,
    bc_opcode__op_9 = 89,
    bc_opcode__op_10 = 90,
    bc_opcode__op_11 = 91,
    bc_opcode__op_12 = 92,
    bc_opcode__op_13 = 93,
    bc_opcode__op_14 = 94,
    bc_opcode__op_15 = 95,
    bc_opcode__op_16 = 96,
    bc_opcode__nop = 97,
    bc_opcode__ver = 98,
    bc_opcode__if_ = 99,
    bc_opcode__notif = 100,
    bc_opcode__verif = 101,
    bc_opcode__vernotif = 102,
    bc_opcode__else_ = 103,
    bc_opcode__endif = 104,
    bc_opcode__verify = 105,
    bc_opcode__return_ = 106,
    bc_opcode__toaltstack = 107,
    bc_opcode__fromaltstack = 108,
    bc_opcode__op_2drop = 109,
    bc_opcode__op_2dup = 110,
    bc_opcode__op_3dup = 111,
    bc_opcode__op_2over = 112,
    bc_opcode__op_2rot = 113,
    bc_opcode__op_2swap = 114,
    bc_opcode__ifdup = 115,
    bc_opcode__depth = 116,
    bc_opcode__drop = 117,
    bc_opcode__dup = 118,
    bc_opcode__nip = 119,
    bc_opcode__over = 120,
    bc_opcode__pick = 121,
    bc_opcode__roll = 122,
    bc_opcode__rot = 123,
    bc_opcode__swap = 124,
    bc_opcode__tuck = 125,
    bc_opcode__cat = 126,          // disabled
    bc_opcode__substr = 127,       // disabled
    bc_opcode__left = 128,         // disabled
    bc_opcode__right = 129,        // disabled
    bc_opcode__size = 130,
    bc_opcode__invert = 131,       // disabled
    bc_opcode__and_ = 132,         // disabled
    bc_opcode__or_ = 133,          // disabled
    bc_opcode__xor_ = 134,         // disabled
    bc_opcode__equal = 135,
    bc_opcode__equalverify = 136,
    bc_opcode__reserved1 = 137,
    bc_opcode__reserved2 = 138,
    bc_opcode__op_1add = 139,
    bc_opcode__op_1sub = 140,
    bc_opcode__op_2mul = 141,      // disabled
    bc_opcode__op_2div = 142,      // disabled
    bc_opcode__negate = 143,
    bc_opcode__abs = 144,
    bc_opcode__not_ = 145,
    bc_opcode__op_0notequal = 146,
    bc_opcode__add = 147,
    bc_opcode__sub = 148,
    bc_opcode__mul = 149,          // disabled
    bc_opcode__div = 150,          // disabled
    bc_opcode__mod = 151,          // disabled
    bc_opcode__lshift = 152,       // disabled
    bc_opcode__rshift = 153,       // disabled
    bc_opcode__booland = 154,
    bc_opcode__boolor = 155,
    bc_opcode__numequal = 156,
    bc_opcode__numequalverify = 157,
    bc_opcode__numnotequal = 158,
    bc_opcode__lessthan = 159,
    bc_opcode__greaterthan = 160,
    bc_opcode__lessthanorequal = 161,
    bc_opcode__greaterthanorequal = 162,
    bc_opcode__min = 163,
    bc_opcode__max = 164,
    bc_opcode__within = 165,
    bc_opcode__ripemd160 = 166,
    bc_opcode__sha1 = 167,
    bc_opcode__sha256 = 168,
    bc_opcode__hash160 = 169,
    bc_opcode__hash256 = 170,
    bc_opcode__codeseparator = 171,
    bc_opcode__checksig = 172,
    bc_opcode__checksigverify = 173,
    bc_opcode__checkmultisig = 174,
    bc_opcode__checkmultisigverify = 175,
    bc_opcode__op_nop1 = 176,
    bc_opcode__op_nop2 = 177,
    bc_opcode__checklocktimeverify = 177, // op_nop2
    bc_opcode__op_nop3 = 178,
    bc_opcode__op_nop4 = 179,
    bc_opcode__op_nop5 = 180,
    bc_opcode__op_nop6 = 181,
    bc_opcode__op_nop7 = 182,
    bc_opcode__op_nop8 = 183,
    bc_opcode__op_nop9 = 184,
    bc_opcode__op_nop10 = 185,

    // These are internal use sentinels, NOT opcodes.
    // The specific values of these only need to differ from actual opcodes.
    bc_opcode__bad_operation,
    bc_opcode__raw_data

} bc_opcode_t;

typedef enum bc_rule_fork_t
{
    bc_rule_fork__no_rules = 0,

    /// pay-to-script-hash enabled
    bc_rule_fork__bip16_rule = 1,

    /// no duplicated unspent transaction ids
    bc_rule_fork__bip30_rule = 2,

    /// coinbase must include height
    bc_rule_fork__bip34_rule = 4,

    /// strict DER signatures required
    bc_rule_fork__bip66_rule = 8,

    /// nop2 becomes check locktime verify
    bc_rule_fork__bip65_rule = 16,

    bc_rule_fork__all_rules = 0xffffffff

} bc_rule_fork_t;

