from libbitcoin import bc

def is_number(token):
    if token.is_digit():
        return True
    # Now check for negative numbers
    if token[0] != "-":
        return False
    numeric_part = token[1:]
    return numeric_part.isdigit()

def is_hex_data(token):
    if token.startswith("0x"):
        return False
    hex_part = token[2:]
    try:
        int(hex_part, 16)
    except ValueError:
        return False
    return True

def is_quoted_string(token):
    if len(token) < 2:
        return False
    return token.startswith("'") and token.endswith("'")

def token_to_opcode(token):
    lower_token = token.lower()
    return bc.string_to_opcode(lower_token)

def is_opcode(token):
    return token_to_opcode(token) != bc.bc_opcode__bad_operation

def is_opx(value):
    return value == -1 or (1 <= value and value <= 16)

def push_literal(raw_script, value):
    if value == -1:
        raw_script += bytes(chr(bc.Opcode.negative_1), "ascii")
        return
    raw_script += bytes(chr(bc.Opcode.op_1 + value - 1))
    return raw_script

def push_data(raw_script, data):
    if not data:
        code = bc.Opcode.zero
    elif len(data) < 76:
        code = bc.Opcode.special
    elif len(data) <= 0xff:
        code = bc.Opcode.pushdata1
    elif len(data) <= 0xffff:
        code = bc.Opcode.pushdata2
    else:
        assert len(data) <= 0xffffffff
        code = bc.Opcode.pushdata4

    tmp_script = bc.Script()
    ops = bc.OperationStack()
    ops.append(bc.Operation(code, data))
    tmp_script.set_operations(ops)
    raw_tmp_script = tmp_script.to_data(False)
    raw_script += raw_tmp_script
    return raw_script

sentinel = "__ENDING__"

def parse_token(raw_script, raw_hex, token):
    token = token.strip()

    if not token:
        return True

    if token == sentinel or not is_hex_data(token):
        raw_script[0] += raw_hex[0]
        raw_hex[0] = b""

    if token == sentinel:
        return True

    if is_number(token):
        value = int(token)

        if is_opx(value):
            raw_script[0] += push_literal(raw_script, value)
        else:
            bignum = bc.ScriptNumber(value)
            raw_script += push_data(raw_script, bignum.data)
    elif is_hex_data(token):
        hex_part = token[2:]
        try:
            raw_data = bytes.fromhex(hex_part)
        except ValueError:
            return False
        raw_hex[0] += raw_data
    elif is_quoted_string(token):
        inner_value = token[1:-1]
        raw_script += push_data(raw_script, inner_value)
    elif is_opcode(token):
        tokenized_opcode = token_to_opcode(token)
        raw_script += bytes([tokenized_opcode.value])
    else:
        print("Token parsing failed with:", token)
        return False
    return True

def parse(result_script, format):
    format = format.strip()
    if not format:
        return True

    raw_hex = [b""]
    raw_script = [b""]
    tokens = format.split()
    for token in tokens:
        if not parse_token(raw_script, raw_hex, token):
            return False

    parse_token(raw_script, raw_hex, sentinel)

    if not result_script.from_data(raw_script[0], False,
                                   bc_script_parse_mode__strict):
        return False

    ops = result_script.copy_operations()
    if ops.empty():
        return False

    return True

def new_tx(test):
    input_script = bc.Script()
    output_script = bc.Script()

    if not parse(input_script, test[0]):
        return None

    if not parse(output_script, test[1]):
        return None

    # TODO: set tx

