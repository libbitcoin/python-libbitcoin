from libbitcoin import bc
import chain.script_data

def is_number(token):
    if token.isdigit():
        return True
    # Now check for negative numbers
    if token[0] != "-":
        return False
    numeric_part = token[1:]
    return numeric_part.isdigit()

def is_hex_data(token):
    if not token.startswith("0x"):
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

def is_opcode(token):
    return bc.opcode_from_string(token) is not None

def is_opx(value):
    return value == -1 or (1 <= value and value <= 16)

def push_literal(value):
    assert is_opx(value)
    if value == -1:
        return bytes(chr(bc.Opcode.negative_1.value), "ascii")
    return bytes(chr(bc.Opcode.op_1.value + value - 1), "ascii")

def push_data(data):
    return bc.Operation.from_data(data).to_data()

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
            raw_script[0] += push_literal(value)
        else:
            bignum = bc.MachineNumber(value)
            raw_script[0] += push_data(bignum.data())
    elif is_hex_data(token):
        hex_part = token[2:]
        try:
            raw_data = bytes.fromhex(hex_part)
        except ValueError:
            return False
        raw_hex[0] += raw_data
    elif is_quoted_string(token):
        inner_value = bytes(token[1:-1], "ascii")
        raw_script[0] += push_data(inner_value)
    elif bc.opcode_from_string(token) is not None:
        out_code = bc.opcode_from_string(token)
        raw_script[0] += bytes([out_code.value])
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

    result = bc.Script.from_data(raw_script[0], False)
    if result is None:
        return False

    result_script[0] = result
    if result_script[0].empty():
        return False

    return True

def new_tx(test, sequence=0):
    tx = bc.Transaction()

    input_script = [bc.Script()]
    if not parse(input_script, test[0]):
        return tx

    output_script = [bc.Script()]
    if not parse(output_script, test[1]):
        return tx

    input = bc.Input()
    input.set_sequence(sequence)
    input.set_script(input_script[0])
    input.previous_output().validation.cache.set_script(output_script[0])

    tx.set_inputs([input])
    return tx

def script__one_hash__literal__same():
    hash_one = bc.hash_literal(
        "0000000000000000000000000000000000000000000000000000000000000001")
    one_hash = bc.HashDigest.from_bytes(
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    assert hash_one == one_hash

def script__from_data__testnet_119058_invalid_op_codes__success():
    raw_script = bytes.fromhex("0130323066643366303435313438356531306633383837363437356630643265396130393739343332353534313766653139316438623963623230653430643863333030326431373463336539306366323433393231383761313037623634373337633937333135633932393264653431373731636565613062323563633534353732653302ae")

    parsed = bc.Script()
    assert parsed.from_data(raw_script, False)

def script__from_data__parse__success():
    raw_script = bytes.fromhex("3045022100ff1fc58dbd608e5e05846a8e6b45a46ad49878aef6879ad1a7cf4c5a7f853683022074a6a10f6053ab3cddc5620d169c7374cd42c1416c51b9744db2c8d9febfb84d01")

    parsed = bc.Script()
    assert parsed.from_data(raw_script, True)

def script__from_data__to_data__roundtrips():
    normal_output_script = bytes.fromhex("76a91406ccef231c2db72526df9338894ccf9355e8f12188ac")

    out_script = bc.Script.from_data(normal_output_script, False)
    assert out_script is not None

    roundtrip = out_script.to_data(False)
    assert roundtrip == normal_output_script

def script__from_data__to_data_weird__roundtrips():
    weird_raw_script = bytes.fromhex(
        "0c49206c69656b20636174732e483045022100c7387f64e1f4"
        "cf654cae3b28a15f7572106d6c1319ddcdc878e636ccb83845"
        "e30220050ebf440160a4c0db5623e0cb1562f46401a7ff5b87"
        "7aa03415ae134e8c71c901534d4f0176519c6375522103b124"
        "c48bbff7ebe16e7bd2b2f2b561aa53791da678a73d2777cc1c"
        "a4619ab6f72103ad6bb76e00d124f07a22680e39debd4dc4bd"
        "b1aa4b893720dd05af3c50560fdd52af67529c63552103b124"
        "c48bbff7ebe16e7bd2b2f2b561aa53791da678a73d2777cc1c"
        "a4619ab6f721025098a1d5a338592bf1e015468ec5a8fafc1f"
        "c9217feb5cb33597f3613a2165e9210360cfabc01d52eaaeb3"
        "976a5de05ff0cfa76d0af42d3d7e1b4c233ee8a00655ed2103"
        "f571540c81fd9dbf9622ca00cfe95762143f2eab6b65150365"
        "bb34ac533160432102bc2b4be1bca32b9d97e2d6fb255504f4"
        "bc96e01aaca6e29bfa3f8bea65d8865855af672103ad6bb76e"
        "00d124f07a22680e39debd4dc4bdb1aa4b893720dd05af3c50"
        "560fddada820a4d933888318a23c28fb5fc67aca8530524e20"
        "74b1d185dbf5b4db4ddb0642848868685174519c6351670068")

    weird = bc.Script.from_data(weird_raw_script, False)
    assert weird is not None

    roundtrip_result = weird.to_data(False)
    assert roundtrip_result == weird_raw_script

def script__factory_from_data_chunk_test():
    raw = bytes.fromhex("76a914fc7b44566256621affb1541cc9d59f08336d276b88ac")
    instance = bc.Script.from_data(raw, False)
    assert instance is not None
    assert instance.is_valid()

def script__from_data__first_byte_invalid_wire_code__success():
    raw = bytes.fromhex(
        "bb566a54e38193e381aee4b896e7958ce381afe496e4babae381abe38288e381"
        "a3e381a6e7ac91e9a194e38292e5a5aae3828fe3828ce3828be7bea9e58b99e3"
        "8292e8a8ade38191e381a6e381afe38184e381aae38184")
    instance = bc.Script.from_data(raw, False)
    assert instance is not None

def script__from_data__internal_invalid_wire_code__success():
    raw = bytes.fromhex(
        "566a54e38193e381aee4b896e7958ce381afe4bb96e4babae381abe38288e381"
        "a3e381a6e7ac91e9a194e38292e5a5aae3828fe3828ce3828be7bea9e58b99e3"
        "8292e8a8ade38191e381a6e381afe38184e381aae38184")
    instance = bc.Script.from_data(raw, False)
    assert instance is not None

def script__native__block_438513_tx__valid():
    #06:21:05.532171 DEBUG [blockchain] Input validation failed (stack false)
    # lib         : false
    # forks       : 62
    # outpoint    : 8e51d775e0896e03149d585c0655b3001da0c55068b0885139ac6ec34cf76ba0:0
    # script      : a914faa558780a5767f9e3be14992a578fc1cbcf483087
    # inpoint     : 6b7f50afb8448c39f4714a73d2b181d3e3233e84670bdfda8f141db668226c54:0
    # transaction : 0100000001a06bf74cc36eac395188b06850c5a01d00b355065c589d14036e89e075d7518e000000009d483045022100ba555ac17a084e2a1b621c2171fa563bc4fb75cd5c0968153f44ba7203cb876f022036626f4579de16e3ad160df01f649ffb8dbf47b504ee56dc3ad7260af24ca0db0101004c50632102768e47607c52e581595711e27faffa7cb646b4f481fe269bd49691b2fbc12106ad6704355e2658b1756821028a5af8284a12848d69a25a0ac5cea20be905848eb645fd03d3b065df88a9117cacfeffffff0158920100000000001976a9149d86f66406d316d44d58cbf90d71179dd8162dd388ac355e2658

    input_index = 0
    forks = bc.RuleFork(62)
    encoded_script = "a914faa558780a5767f9e3be14992a578fc1cbcf483087"
    encoded_tx = "0100000001a06bf74cc36eac395188b06850c5a01d00b355065c589d14036e89e075d7518e000000009d483045022100ba555ac17a084e2a1b621c2171fa563bc4fb75cd5c0968153f44ba7203cb876f022036626f4579de16e3ad160df01f649ffb8dbf47b504ee56dc3ad7260af24ca0db0101004c50632102768e47607c52e581595711e27faffa7cb646b4f481fe269bd49691b2fbc12106ad6704355e2658b1756821028a5af8284a12848d69a25a0ac5cea20be905848eb645fd03d3b065df88a9117cacfeffffff0158920100000000001976a9149d86f66406d316d44d58cbf90d71179dd8162dd388ac355e2658"

    decoded_tx = bytes.fromhex(encoded_tx)
    decoded_script = bytes.fromhex(encoded_script)

    tx = bc.Transaction.from_data(decoded_tx)
    assert tx is not None

    input = tx.inputs()[input_index]
    # TODO: incomplete unit test. Need validation cache first.

def script__bip16__valid():
    for test in chain.script_data.valid_bip16_scripts:
        tx = new_tx(test)
        assert tx.is_valid(), test[2]
        assert tx.inputs(), test[2]

        # These are valid prior to and after BIP16 activation.
        assert bc.Script.verify(tx, 0, bc.RuleFork.no_rules) == \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.bip16_rule) == \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.all_rules) == \
            bc.Error.success, test[2]

def script__bip16__invalidated():
    for test in chain.script_data.invalidated_bip16_scripts:
        tx = new_tx(test)
        assert tx.is_valid(), test[2]
        assert tx.inputs(), test[2]

        # These are valid prior to BIP16 activation and invalid after.
        assert bc.Script.verify(tx, 0, bc.RuleFork.no_rules) == \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.bip16_rule) != \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.all_rules) != \
            bc.Error.success, test[2]

def script__bip65__valid():
    for test in chain.script_data.valid_bip65_scripts:
        tx = new_tx(test, 42)
        assert tx.is_valid(), test[2]
        assert tx.inputs(), test[2]

        tx.set_locktime(99)
        
        # These are valid prior to and after BIP65 activation.
        assert bc.Script.verify(tx, 0, bc.RuleFork.no_rules) == \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.bip65_rule) == \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.all_rules) == \
            bc.Error.success, test[2]

def script__bip65__invalid():
    for test in chain.script_data.invalid_bip65_scripts:
        tx = new_tx(test, 42)
        assert tx.is_valid(), test[2]
        assert tx.inputs(), test[2]

        tx.set_locktime(99)

        # These are invalid prior to and after BIP65 activation.
        assert bc.Script.verify(tx, 0, bc.RuleFork.no_rules) != \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.bip65_rule) != \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.all_rules) != \
            bc.Error.success, test[2]

def script__bip65__invalidated():
    for test in chain.script_data.invalidated_bip65_scripts:
        tx = new_tx(test, 42)
        assert tx.is_valid(), test[2]
        assert tx.inputs(), test[2]

        tx.set_locktime(99)

        # These are valid prior to and after BIP65 activation.
        assert bc.Script.verify(tx, 0, bc.RuleFork.no_rules) == \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.bip65_rule) != \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.all_rules) != \
            bc.Error.success, test[2]

# These are scripts potentially affected by bip66 (but should not be).
def script__multisig__valid():
    for test in chain.script_data.valid_multisig_scripts:
        tx = new_tx(test, 42)
        assert tx.is_valid(), test[2]
        assert tx.inputs(), test[2]

        # These are always valid.
        assert bc.Script.verify(tx, 0, bc.RuleFork.no_rules) == \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.bip66_rule) == \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.all_rules) == \
            bc.Error.success, test[2]

# These are scripts potentially affected by bip66 (but should not be).
def script__multisig__invalid():
    for test in chain.script_data.invalid_multisig_scripts:
        tx = new_tx(test)
        assert tx.is_valid(), test[2]
        assert tx.inputs(), test[2]

        # These are always invalid.
        assert bc.Script.verify(tx, 0, bc.RuleFork.no_rules) != \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.bip66_rule) != \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.all_rules) != \
            bc.Error.success, test[2]

def script__context_free__valid():
    for test in chain.script_data.valid_context_free_scripts:
        tx = new_tx(test)
        assert tx.is_valid(), test[2]
        assert tx.inputs(), test[2]

        # These are always valid.
        assert bc.Script.verify(tx, 0, bc.RuleFork.no_rules) == \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.all_rules) == \
            bc.Error.success, test[2]

def script__context_free__invalid():
    for test in chain.script_data.invalid_context_free_scripts:
        tx = new_tx(test)
        assert tx.is_valid(), test[2]
        assert tx.inputs(), test[2]

        # These are always valid.
        assert bc.Script.verify(tx, 0, bc.RuleFork.no_rules) != \
            bc.Error.success, test[2]
        assert bc.Script.verify(tx, 0, bc.RuleFork.all_rules) != \
            bc.Error.success, test[2]

# These are special tests for checksig.
def script__checksig__uses_one_hash():
    # input 315ac7d4c26d69668129cc352851d9389b4a6868f1509c6c8b66bead11e2619f:1
    tx_data = bytes.fromhex("0100000002dc38e9359bd7da3b58386204e186d9408685f427f5e513666db735aa8a6b2169000000006a47304402205d8feeb312478e468d0b514e63e113958d7214fa572acd87079a7f0cc026fc5c02200fa76ea05bf243af6d0f9177f241caf606d01fcfd5e62d6befbca24e569e5c27032102100a1a9ca2c18932d6577c58f225580184d0e08226d41959874ac963e3c1b2feffffffffdc38e9359bd7da3b58386204e186d9408685f427f5e513666db735aa8a6b2169010000006b4830450220087ede38729e6d35e4f515505018e659222031273b7366920f393ee3ab17bc1e022100ca43164b757d1a6d1235f13200d4b5f76dd8fda4ec9fc28546b2df5b1211e8df03210275983913e60093b767e85597ca9397fb2f418e57f998d6afbbc536116085b1cbffffffff0140899500000000001976a914fcc9b36d38cf55d7d5b4ee4dddb6b2c17612f48c88ac00000000")
    parent_tx = bc.Transaction.from_data(tx_data)

    distinguished = bytes.fromhex("30450220087ede38729e6d35e4f515505018e659222031273b7366920f393ee3ab17bc1e022100ca43164b757d1a6d1235f13200d4b5f76dd8fda4ec9fc28546b2df5b1211e8df")

    pubkey = bytes.fromhex("0275983913e60093b767e85597ca9397fb2f418e57f998d6afbbc536116085b1cb")

    script_data = bytes.fromhex("76a91433cef61749d11ba2adf091a5e045678177fe3a6d88ac")

    script_code = bc.Script.from_data(script_data, False)
    assert script_code is not None

    strict = True
    input_index = 1
    signature = bc.EcSignature.from_der(distinguished, strict)
    assert signature is not None
    assert bc.Script.check_signature(
        signature, bc.SighashAlgorithm.single, pubkey,
        script_code, parent_tx, input_index)

def script__checksig__normal():
    # input 315ac7d4c26d69668129cc352851d9389b4a6868f1509c6c8b66bead11e2619f:0
    tx_data = bytes.fromhex("0100000002dc38e9359bd7da3b58386204e186d9408685f427f5e513666db735aa8a6b2169000000006a47304402205d8feeb312478e468d0b514e63e113958d7214fa572acd87079a7f0cc026fc5c02200fa76ea05bf243af6d0f9177f241caf606d01fcfd5e62d6befbca24e569e5c27032102100a1a9ca2c18932d6577c58f225580184d0e08226d41959874ac963e3c1b2feffffffffdc38e9359bd7da3b58386204e186d9408685f427f5e513666db735aa8a6b2169010000006b4830450220087ede38729e6d35e4f515505018e659222031273b7366920f393ee3ab17bc1e022100ca43164b757d1a6d1235f13200d4b5f76dd8fda4ec9fc28546b2df5b1211e8df03210275983913e60093b767e85597ca9397fb2f418e57f998d6afbbc536116085b1cbffffffff0140899500000000001976a914fcc9b36d38cf55d7d5b4ee4dddb6b2c17612f48c88ac00000000")
    parent_tx = bc.Transaction.from_data(tx_data)

    distinguished = bytes.fromhex("304402205d8feeb312478e468d0b514e63e113958d7214fa572acd87079a7f0cc026fc5c02200fa76ea05bf243af6d0f9177f241caf606d01fcfd5e62d6befbca24e569e5c27")

    pubkey = bytes.fromhex("02100a1a9ca2c18932d6577c58f225580184d0e08226d41959874ac963e3c1b2fe")

    script_data = bytes.fromhex("76a914fcc9b36d38cf55d7d5b4ee4dddb6b2c17612f48c88ac")

    script_code = bc.Script.from_data(script_data, False)
    assert script_code is not None

    strict = True
    input_index = 0
    signature = bc.EcSignature.from_der(distinguished, strict)
    assert signature is not None
    assert bc.Script.check_signature(
        signature, bc.SighashAlgorithm.single, pubkey,
        script_code, parent_tx, input_index)

def script__create_endorsement__single_input_single_output__expected():
    tx_data = bytes.fromhex("0100000001b3807042c92f449bbf79b33ca59d7dfec7f4cc71096704a9c526dddf496ee0970100000000ffffffff01905f0100000000001976a91418c0bd8d1818f1bf99cb1df2269c645318ef7b7388ac00000000")
    new_tx = bc.Transaction.from_data(tx_data)

    prevout_script = bc.Script.from_string("dup hash160 [88350574280395ad2c3e2ee20e322073d94e5e40] equalverify checksig")
    assert prevout_script is not None

    secret = bc.EcSecret.from_string("ce8f4b713ffdd2658900845251890f30371856be201cd1f5b3d970f793634333", True)

    input_index = 0
    sighash_type = bc.SighashAlgorithm.all
    out = bc.Script.create_endorsement(secret, prevout_script, new_tx,
                                       input_index, sighash_type)
    assert out is not None

    assert out.hex() == "3045022100e428d3cc67a724cb6cfe8634aa299e58f189d9c46c02641e936c40cc16c7e8ed0220083949910fe999c21734a1f33e42fca15fb463ea2e08f0a1bccd952aacaadbb801"

def script__create_endorsement__single_input_no_output__expected():
    tx_data = bytes.fromhex("0100000001b3807042c92f449bbf79b33ca59d7dfec7f4cc71096704a9c526dddf496ee0970000000000ffffffff0000000000")
    new_tx = bc.Transaction.from_data(tx_data)

    prevout_script = bc.Script.from_string("dup hash160 [88350574280395ad2c3e2ee20e322073d94e5e40] equalverify checksig")
    assert prevout_script is not None

    secret = bc.EcSecret.from_string("ce8f4b713ffdd2658900845251890f30371856be201cd1f5b3d970f793634333", True)

    input_index = 0
    sighash_type = bc.SighashAlgorithm.all
    out = bc.Script.create_endorsement(secret, prevout_script, new_tx,
                                       input_index, sighash_type)
    assert out is not None

    assert out.hex() == "3045022100ba57820be5f0b93a0d5b880fbf2a86f819d959ecc24dc31b6b2d4f6ed286f253022071ccd021d540868ee10ca7634f4d270dfac7aea0d5912cf2b104111ac9bc756b01"

def script__generate_signature_hash__all__expected():
    tx_data = bytes.fromhex("0100000001b3807042c92f449bbf79b33ca59d7dfec7f4cc71096704a9c526dddf496ee0970000000000ffffffff0000000000")
    new_tx = bc.Transaction.from_data(tx_data)

    prevout_script = bc.Script.from_string("dup hash160 [88350574280395ad2c3e2ee20e322073d94e5e40] equalverify checksig")
    assert prevout_script is not None

    input_index = 0
    sighash_type = bc.SighashAlgorithm.all
    sighash = bc.Script.generate_signature_hash(new_tx, input_index,
                                                prevout_script, sighash_type)
    assert sighash.data.hex() == "f89572635651b2e4f89778350616989183c98d1a721c911324bf9f17a0cf5bf0"

script__one_hash__literal__same()
script__from_data__testnet_119058_invalid_op_codes__success()
script__from_data__parse__success()
script__from_data__to_data__roundtrips()
script__from_data__to_data_weird__roundtrips()
script__factory_from_data_chunk_test()
script__from_data__first_byte_invalid_wire_code__success()
script__from_data__internal_invalid_wire_code__success()
script__native__block_438513_tx__valid()
script__bip16__valid()
script__bip16__invalidated()
script__bip65__valid()
script__bip65__invalid()
script__bip65__invalidated()
script__multisig__valid()
script__multisig__invalid()
script__context_free__valid()
script__context_free__invalid()
script__checksig__uses_one_hash()
script__checksig__normal()
script__create_endorsement__single_input_single_output__expected()
script__create_endorsement__single_input_no_output__expected()
script__generate_signature_hash__all__expected()

