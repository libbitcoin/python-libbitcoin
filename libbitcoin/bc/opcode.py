from enum import Enum
from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.string import String

class Opcode(Enum):
    zero = 0
    special = 1
    pushdata1 = 76
    pushdata2 = 77
    pushdata4 = 78
    negative_1 = 79
    reserved = 80  # does nothing
    op_1 = 81
    op_2 = 82
    op_3 = 83
    op_4 = 84
    op_5 = 85
    op_6 = 86
    op_7 = 87
    op_8 = 88
    op_9 = 89
    op_10 = 90
    op_11 = 91
    op_12 = 92
    op_13 = 93
    op_14 = 94
    op_15 = 95
    op_16 = 96
    nop = 97
    ver = 98
    if_ = 99
    notif = 100
    verif = 101
    vernotif = 102
    else_ = 103
    endif = 104
    verify = 105
    return_ = 106
    toaltstack = 107
    fromaltstack = 108
    op_2drop = 109
    op_2dup = 110
    op_3dup = 111
    op_2over = 112
    op_2rot = 113
    op_2swap = 114
    ifdup = 115
    depth = 116
    drop = 117
    dup = 118
    nip = 119
    over = 120
    pick = 121
    roll = 122
    rot = 123
    swap = 124
    tuck = 125
    cat = 126          # disabled
    substr = 127       # disabled
    left = 128         # disabled
    right = 129        # disabled
    size = 130
    invert = 131       # disabled
    and_ = 132         # disabled
    or_ = 133          # disabled
    xor_ = 134         # disabled
    equal = 135
    equalverify = 136
    reserved1 = 137
    reserved2 = 138
    op_1add = 139
    op_1sub = 140
    op_2mul = 141      # disabled
    op_2div = 142      # disabled
    negate = 143
    abs = 144
    not_ = 145
    op_0notequal = 146
    add = 147
    sub = 148
    mul = 149          # disabled
    div = 150          # disabled
    mod = 151          # disabled
    lshift = 152       # disabled
    rshift = 153       # disabled
    booland = 154
    boolor = 155
    numequal = 156
    numequalverify = 157
    numnotequal = 158
    lessthan = 159
    greaterthan = 160
    lessthanorequal = 161
    greaterthanorequal = 162
    min = 163
    max = 164
    within = 165
    ripemd160 = 166
    sha1 = 167
    sha256 = 168
    hash160 = 169
    hash256 = 170
    codeseparator = 171
    checksig = 172
    checksigverify = 173
    checkmultisig = 174
    checkmultisigverify = 175
    op_nop1 = 176
    op_nop2 = 177
    checklocktimeverify = op_nop2
    op_nop3 = 178
    op_nop4 = 179
    op_nop5 = 180
    op_nop6 = 181
    op_nop7 = 182
    op_nop8 = 183
    op_nop9 = 184
    op_nop10 = 185
    # These are internal use sentinels NOT opcodes.
    # The specific values of these only need to differ from actual opcodes.
    bad_operation = 186
    raw_data = 187

def within_op_n(code):
    """Determine if code is in the op_n range."""
    return lib.bc_within_op_n(code.value) == 1

def decode_op_n(code):
    """Return the op_n index (i.e. value of n)."""
    return lib.bc_decode_op_n(code.value)

def data_to_opcode(value):
    """Convert data to an opcode."""
    value = DataChunk(value)
    return Opcode(lib.bc_data_to_opcode(value._obj))

def string_to_opcode(value):
    """Convert a string to an opcode."""
    value = bytes(value, "ascii")
    return Opcode(lib.bc_string_to_opcode(value))

def opcode_to_string(value, flags):
    """Convert an opcode to a string."""
    obj = lib.bc_opcode_to_string(value.value, flags)
    return str(String(obj))

