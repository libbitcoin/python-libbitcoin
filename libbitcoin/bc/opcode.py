from enum import Enum
from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.string_ import String

class Opcode(Enum):
    zero = lib.bc_opcode__zero
    special = lib.bc_opcode__special
    pushdata1 = lib.bc_opcode__pushdata1
    pushdata2 = lib.bc_opcode__pushdata2
    pushdata4 = lib.bc_opcode__pushdata4
    negative_1 = lib.bc_opcode__negative_1
    reserved = lib.bc_opcode__reserved
    op_1 = lib.bc_opcode__op_1
    op_2 = lib.bc_opcode__op_2
    op_3 = lib.bc_opcode__op_3
    op_4 = lib.bc_opcode__op_4
    op_5 = lib.bc_opcode__op_5
    op_6 = lib.bc_opcode__op_6
    op_7 = lib.bc_opcode__op_7
    op_8 = lib.bc_opcode__op_8
    op_9 = lib.bc_opcode__op_9
    op_10 = lib.bc_opcode__op_10
    op_11 = lib.bc_opcode__op_11
    op_12 = lib.bc_opcode__op_12
    op_13 = lib.bc_opcode__op_13
    op_14 = lib.bc_opcode__op_14
    op_15 = lib.bc_opcode__op_15
    op_16 = lib.bc_opcode__op_16
    nop = lib.bc_opcode__nop
    ver = lib.bc_opcode__ver
    if_ = lib.bc_opcode__if_
    notif = lib.bc_opcode__notif
    verif = lib.bc_opcode__verif
    vernotif = lib.bc_opcode__vernotif
    else_ = lib.bc_opcode__else_
    endif = lib.bc_opcode__endif
    verify = lib.bc_opcode__verify
    return_ = lib.bc_opcode__return_
    toaltstack = lib.bc_opcode__toaltstack
    fromaltstack = lib.bc_opcode__fromaltstack
    op_2drop = lib.bc_opcode__op_2drop
    op_2dup = lib.bc_opcode__op_2dup
    op_3dup = lib.bc_opcode__op_3dup
    op_2over = lib.bc_opcode__op_2over
    op_2rot = lib.bc_opcode__op_2rot
    op_2swap = lib.bc_opcode__op_2swap
    ifdup = lib.bc_opcode__ifdup
    depth = lib.bc_opcode__depth
    drop = lib.bc_opcode__drop
    dup = lib.bc_opcode__dup
    nip = lib.bc_opcode__nip
    over = lib.bc_opcode__over
    pick = lib.bc_opcode__pick
    roll = lib.bc_opcode__roll
    rot = lib.bc_opcode__rot
    swap = lib.bc_opcode__swap
    tuck = lib.bc_opcode__tuck
    cat = lib.bc_opcode__cat
    substr = lib.bc_opcode__substr
    left = lib.bc_opcode__left
    right = lib.bc_opcode__right
    size = lib.bc_opcode__size
    invert = lib.bc_opcode__invert
    and_ = lib.bc_opcode__and_
    or_ = lib.bc_opcode__or_
    xor_ = lib.bc_opcode__xor_
    equal = lib.bc_opcode__equal
    equalverify = lib.bc_opcode__equalverify
    reserved1 = lib.bc_opcode__reserved1
    reserved2 = lib.bc_opcode__reserved2
    op_1add = lib.bc_opcode__op_1add
    op_1sub = lib.bc_opcode__op_1sub
    op_2mul = lib.bc_opcode__op_2mul
    op_2div = lib.bc_opcode__op_2div
    negate = lib.bc_opcode__negate
    abs = lib.bc_opcode__abs
    not_ = lib.bc_opcode__not_
    op_0notequal = lib.bc_opcode__op_0notequal
    add = lib.bc_opcode__add
    sub = lib.bc_opcode__sub
    mul = lib.bc_opcode__mul
    div = lib.bc_opcode__div
    mod = lib.bc_opcode__mod
    lshift = lib.bc_opcode__lshift
    rshift = lib.bc_opcode__rshift
    booland = lib.bc_opcode__booland
    boolor = lib.bc_opcode__boolor
    numequal = lib.bc_opcode__numequal
    numequalverify = lib.bc_opcode__numequalverify
    numnotequal = lib.bc_opcode__numnotequal
    lessthan = lib.bc_opcode__lessthan
    greaterthan = lib.bc_opcode__greaterthan
    lessthanorequal = lib.bc_opcode__lessthanorequal
    greaterthanorequal = lib.bc_opcode__greaterthanorequal
    min = lib.bc_opcode__min
    max = lib.bc_opcode__max
    within = lib.bc_opcode__within
    ripemd160 = lib.bc_opcode__ripemd160
    sha1 = lib.bc_opcode__sha1
    sha256 = lib.bc_opcode__sha256
    hash160 = lib.bc_opcode__hash160
    hash256 = lib.bc_opcode__hash256
    codeseparator = lib.bc_opcode__codeseparator
    checksig = lib.bc_opcode__checksig
    checksigverify = lib.bc_opcode__checksigverify
    checkmultisig = lib.bc_opcode__checkmultisig
    checkmultisigverify = lib.bc_opcode__checkmultisigverify
    op_nop1 = lib.bc_opcode__op_nop1
    op_nop2 = lib.bc_opcode__op_nop2
    checklocktimeverify = lib.bc_opcode__checklocktimeverify
    op_nop3 = lib.bc_opcode__op_nop3
    op_nop4 = lib.bc_opcode__op_nop4
    op_nop5 = lib.bc_opcode__op_nop5
    op_nop6 = lib.bc_opcode__op_nop6
    op_nop7 = lib.bc_opcode__op_nop7
    op_nop8 = lib.bc_opcode__op_nop8
    op_nop9 = lib.bc_opcode__op_nop9
    op_nop10 = lib.bc_opcode__op_nop10
    bad_operation = lib.bc_opcode__bad_operation
    raw_data = lib.bc_opcode__raw_data

def opcode_to_string(value, active_forks):
    """Convert the opcode to a mnemonic string."""
    obj = lib.bc_opcode_to_string(value.value, active_forks)
    return str(String(obj))

def opcode_from_string(value):
    """Convert a string to an opcode."""
    if isinstance(value, str):
        value = bytes(value, "ascii")
    out_code = ffi.new("enum bc_opcode_t*")
    if not lib.bc_opcode_from_string(out_code, value):
        return None
    return Opcode(out_code[0])

def opcode_to_hexadecimal(code):
    """Convert any opcode to a string hexadecimal representation."""
    obj = lib.bc_opcode_to_hexadecimal(value.value)
    return str(String(obj))

def opcode_from_hexadecimal(value):
    """Convert any hexadecimal byte to an opcode."""
    if isinstance(value, str):
        value = bytes(value, "ascii")
    out_code = ffi.new("enum bc_opcode_t*")
    if not lib.bc_opcode_from_hexadecimal(out_code, value):
        return None
    return Opcode(out_code[0])

