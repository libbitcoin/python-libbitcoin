from libbitcoin import bc

def transaction__constructor_1__always__returns_default_initialized():
    instance = bc.Transaction()
    assert not instance.is_valid()

TX0 = \
"f08e44a96bfb5ae63eda1a6620adae37ee37ee4777fb0336e1bbbc4de65310fc" \
"010000006a473044022050d8368cacf9bf1b8fb1f7cfd9aff63294789eb17601" \
"39e7ef41f083726dadc4022067796354aba8f2e02363c5e510aa7e2830b11547" \
"2fb31de67d16972867f13945012103e589480b2f746381fca01a9b12c517b7a4" \
"82a203c8b2742985da0ac72cc078f2ffffffff"

TX0_LAST_OUTPUT = \
"f0c9c467000000001976a914d9d78e26df4e4601cf9b26d09c7b280ee764469f88ac"

TX1 = \
"0100000001f08e44a96bfb5ae63eda1a6620adae37ee37ee4777fb0336e1bbbc" \
"4de65310fc010000006a473044022050d8368cacf9bf1b8fb1f7cfd9aff63294" \
"789eb1760139e7ef41f083726dadc4022067796354aba8f2e02363c5e510aa7e" \
"2830b115472fb31de67d16972867f13945012103e589480b2f746381fca01a9b" \
"12c517b7a482a203c8b2742985da0ac72cc078f2ffffffff02f0c9c467000000" \
"001976a914d9d78e26df4e4601cf9b26d09c7b280ee764469f88ac80c4600f00" \
"0000001976a9141ee32412020a324b93b1a1acfdfff6ab9ca8fac288ac000000" \
"00"

TX1_HASH = \
"bf7c3f5a69a78edd81f3eff7e93a37fb2d7da394d48db4d85e7e5353b9b8e270"

TX3_WIRE_SERIALIZED = \
"010000000209e300a61db28e4fd3562aec52647646fc55aa3e3f7d824f20f451" \
"a45db8c958010000006a4730440220364484206d2d3977373a82135cbdb78f20" \
"0e2160ec2636c9f080424a61748d15022056c9729b9fbd5c04170a7bb63b1d1b" \
"02da183fa3605864666dba6e216c3ce9270121027d4b693a2851541b1e393732" \
"0c5e4173ea8ab3f152f7a7fa96dbb936d2cff73dffffffff1cbb3eb855334221" \
"0c67e27dab3c2e72a9c0937b20dc6fe4d08d209fc4c2f163000000006a473044" \
"02207bc1940e12ec94544b7080518f73840f9bd191bd5fcb6b00f69a57a58658" \
"33bc02201bd759d978305e4346b39a9ee8b38043888621748dd1f8ab822df542" \
"427e49d6012102a17da2659b6149fb281a675519b5fd64dd80699dccd509f76e" \
"655699f2f625efffffffff021dc05c00000000001976a914e785da41a84114af" \
"0762c5a6f9e5b78ff730581988ac70e0cf02000000001976a914607a10e5b5f5" \
"3610341db013e77ba7c317a10c9088ac00000000"

TX3_STORE_SERIALIZED = \
"010000000000000002ffffffff1dc05c00000000001976a914e785da41a84114" \
"af0762c5a6f9e5b78ff730581988acffffffff70e0cf02000000001976a91460" \
"7a10e5b5f53610341db013e77ba7c317a10c9088ac0209e300a61db28e4fd356" \
"2aec52647646fc55aa3e3f7d824f20f451a45db8c958010000006a4730440220" \
"364484206d2d3977373a82135cbdb78f200e2160ec2636c9f080424a61748d15" \
"022056c9729b9fbd5c04170a7bb63b1d1b02da183fa3605864666dba6e216c3c" \
"e9270121027d4b693a2851541b1e3937320c5e4173ea8ab3f152f7a7fa96dbb9" \
"36d2cff73dffffffff1cbb3eb8553342210c67e27dab3c2e72a9c0937b20dc6f" \
"e4d08d209fc4c2f163000000006a47304402207bc1940e12ec94544b7080518f" \
"73840f9bd191bd5fcb6b00f69a57a5865833bc02201bd759d978305e4346b39a" \
"9ee8b38043888621748dd1f8ab822df542427e49d6012102a17da2659b6149fb" \
"281a675519b5fd64dd80699dccd509f76e655699f2f625efffffffff"

TX4 = \
"010000000364e62ad837f29617bafeae951776e7a6b3019b2da37827921548d1" \
"a5efcf9e5c010000006b48304502204df0dc9b7f61fbb2e4c8b0e09f3426d625" \
"a0191e56c48c338df3214555180eaf022100f21ac1f632201154f3c69e1eadb5" \
"9901a34c40f1127e96adc31fac6ae6b11fb4012103893d5a06201d5cf61400e9" \
"6fa4a7514fc12ab45166ace618d68b8066c9c585f9ffffffff54b755c39207d4" \
"43fd96a8d12c94446a1c6f66e39c95e894c23418d7501f681b010000006b4830" \
"4502203267910f55f2297360198fff57a3631be850965344370f732950b47795" \
"737875022100f7da90b82d24e6e957264b17d3e5042bab8946ee5fc676d15d91" \
"5da450151d36012103893d5a06201d5cf61400e96fa4a7514fc12ab45166ace6" \
"18d68b8066c9c585f9ffffffff0aa14d394a1f0eaf0c4496537f8ab9246d9663" \
"e26acb5f308fccc734b748cc9c010000006c493046022100d64ace8ec2d5feeb" \
"3e868e82b894202db8cb683c414d806b343d02b7ac679de7022100a2dcd39940" \
"dd28d4e22cce417a0829c1b516c471a3d64d11f2c5d754108bdc0b012103893d" \
"5a06201d5cf61400e96fa4a7514fc12ab45166ace618d68b8066c9c585f9ffff" \
"ffff02c0e1e400000000001976a914884c09d7e1f6420976c40e040c30b2b622" \
"10c3d488ac20300500000000001976a914905f933de850988603aafeeb2fd7fc" \
"e61e66fe5d88ac00000000"

TX4_HASH = \
"8a6d9302fbe24f0ec756a94ecfc837eaffe16c43d1e68c62dfe980d99eea556f"

TX4_TEXT = \
"Transaction:\n" \
"\tversion = 1\n" \
"\tlocktime = 0\n" \
"Inputs:\n" \
"\thash = 5c9ecfefa5d14815922778a32d9b01b3a6e7761795aefeba1796f237d82ae664\n" \
"\tindex = 1\n" \
"\t[304502204df0dc9b7f61fbb2e4c8b0e09f3426d625a0191e56c48c338df3214555180eaf022100f21ac1f632201154f3c69e1eadb59901a34c40f1127e96adc31fac6ae6b11fb401] [03893d5a06201d5cf61400e96fa4a7514fc12ab45166ace618d68b8066c9c585f9]\n" \
"\tsequence = 4294967295\n" \
"\thash = 1b681f50d71834c294e8959ce3666f1c6a44942cd1a896fd43d40792c355b754\n" \
"\tindex = 1\n" \
"\t[304502203267910f55f2297360198fff57a3631be850965344370f732950b47795737875022100f7da90b82d24e6e957264b17d3e5042bab8946ee5fc676d15d915da450151d3601] [03893d5a06201d5cf61400e96fa4a7514fc12ab45166ace618d68b8066c9c585f9]\n" \
"\tsequence = 4294967295\n" \
"\thash = 9ccc48b734c7cc8f305fcb6ae263966d24b98a7f5396440caf0e1f4a394da10a\n" \
"\tindex = 1\n" \
"\t[3046022100d64ace8ec2d5feeb3e868e82b894202db8cb683c414d806b343d02b7ac679de7022100a2dcd39940dd28d4e22cce417a0829c1b516c471a3d64d11f2c5d754108bdc0b01] [03893d5a06201d5cf61400e96fa4a7514fc12ab45166ace618d68b8066c9c585f9]\n" \
"\tsequence = 4294967295\n" \
"Outputs:\n" \
"\tvalue = 15000000\n" \
"\tdup hash160 [884c09d7e1f6420976c40e040c30b2b62210c3d4] equalverify checksig\n" \
"\tvalue = 340000\n" \
"\tdup hash160 [905f933de850988603aafeeb2fd7fce61e66fe5d] equalverify checksig\n\n"

TX5 = \
"01000000023562c207a2a505820324aa03b769ee9c04a221eff59fdab6d52c312544a" \
"c4b21020000006a473044022075d3dd4cd26137f50d1b8c18b5ecbd13b7309b801f62" \
"83ebb951b137972d6e5b02206776f5e3acb2d996a9553f2438a4d2566c1fd786d9075" \
"5a5bca023bd9ae3945b0121029caef1b63490b7deabc9547e3e5d8b13c004b4bfd04d" \
"fae270874d569e5b89a8ffffffff8593568e460593c3dd30a470977a14928be6a29c6" \
"14a644c531471a773a63601020000006a47304402201fd9ea7dc62628ea82ff7b38cc" \
"90b3f2aa8c9ae25aa575600de38c79eafc925602202ca57bcd29d38a3e6aebd6809f7" \
"be4379d86f173b2ad2d42892dcb1dccca14b60121029caef1b63490b7deabc9547e3e" \
"5d8b13c004b4bfd04dfae270874d569e5b89a8ffffffff01763d0300000000001976a" \
"914e0d40d609d0282cc97314e454d194f65c16c257888ac00000000"

TX6 = \
"010000000100000000000000000000000000000000000000000000000000000000000" \
"00000ffffffff23039992060481e1e157082800def50009dfdc102f42697446757279" \
"2f5345475749542f00000000015b382d4b000000001976a9148cf4f6175b2651dcdff" \
"0051970a917ea10189c2d88ac00000000"

TX7 = \
"0100000001b63634c25f23018c18cbb24ad503672fe7c5edc3fef193ec0f581dd" \
"b27d4e401490000006a47304402203b361bfb7e189c77379d6ffc90babe1b9658" \
"39d0b9b60966ade0c4b8de28385f022057432fe6f8f530c54d3513e41da6fb138" \
"fba2440c877cd2bfb0c94cdb5610fbe0121020d2d76d6db0d1c0bda17950f6468" \
"6e4bf42481337707e9a81bbe48458cfc8389ffffffff010000000000000000566" \
"a54e38193e381aee4b896e7958ce381afe4bb96e4babae381abe38288e381a3e3" \
"81a6e7ac91e9a194e38292e5a5aae3828fe3828ce3828be7bea9e58b99e38292e" \
"8a8ade38191e381a6e381afe38184e381aae3818400000000"

TX7_HASH = \
"cb1e303db604f066225eb14d59d3f8d2231200817bc9d4610d2802586bd93f8a"

def transaction__constructor_2__valid_input__returns_input_initialized():
    version = 2345
    locktime = 4568656

    input = bc.Input.from_data(bytes.fromhex(TX0))
    output = bc.Output.from_data(bytes.fromhex(TX0_LAST_OUTPUT))
    assert input is not None
    assert output is not None

    instance = bc.Transaction.from_tuple(version, locktime, [input], [output])
    assert instance is not None
    assert instance.is_valid()
    assert version == instance.version()
    assert locktime == instance.locktime()

def transaction__constructor_4__valid_input__returns_input_initialized():
    raw_tx = bytes.fromhex(TX1)
    expected = bc.Transaction.from_data(raw_tx)

    instance = expected.copy()
    assert instance is not None
    assert instance.is_valid()
    assert expected == instance

def transaction__constructor_6__valid_input__returns_input_initialized():
    raw_tx = bytes.fromhex(TX1)
    expected = bc.Transaction.from_data(raw_tx)
    expected_hash = bc.hash_literal(TX1_HASH)

    instance = expected.copy(expected_hash)
    assert instance is not None
    assert instance.is_valid()
    assert expected_hash == instance.hash()

def transaction__is_coinbase__empty_inputs__returns_false():
    instance = bc.Transaction()
    assert not instance.is_coinbase()

def transaction__is_coinbase__with_coinbase_input__returns_true():
    input = bc.Input()
    input.set_previous_output(bc.OutputPoint.from_tuple(bc.null_hash,
                                                        bc.max_input_sequence))
    instance = bc.Transaction()
    instance.set_inputs([input])
    assert instance.is_coinbase()

def transaction__is_final__locktime_zero__returns_true():
    height = 100
    time = 100
    instance = bc.Transaction()
    instance.set_locktime(0)
    assert instance.is_final(height, time)

def transaction__is_final__locktime_less_block_time_greater_threshold__returns_true():
    height = bc.locktime_threshold + 100
    time = 100
    instance = bc.Transaction()
    instance.set_locktime(bc.locktime_threshold + 50)
    assert instance.is_final(height, time)

def transaction__is_final__locktime_less_block_height_less_threshold_returns_true():
    height = 100
    time = 100
    instance = bc.Transaction()
    instance.set_locktime(50)
    assert instance.is_final(height, time)

def transaction__is_final__locktime_input_not_final__returns_false():
    height = 100
    time = 100
    instance = bc.Transaction()
    instance.set_locktime(101)
    input = bc.Input()
    input.sequence = 1
    instance.set_inputs([input])
    assert not instance.is_final(height, time)

def transaction__is_final__locktime_inputs_final__returns_true():
    height = 100
    time = 100
    input = bc.Input()
    input.set_sequence(bc.max_input_sequence)
    instance = bc.Transaction.from_tuple(0, 101, [input], [])
    assert instance.is_final(height, time)

def transaction__is_locktime_conflict__locktime_zero__returns_false():
    instance = bc.Transaction()
    instance.set_locktime(0)
    assert not instance.is_locktime_conflict()

def transaction__is_locktime_conflict__input_sequence_not_maximum__returns_false():
    input = bc.Input()
    input.set_sequence(1)
    instance = bc.Transaction.from_tuple(0, 2143, [input], [])
    assert not instance.is_locktime_conflict()

def transaction__is_locktime_conflict__no_inputs__returns_true():
    instance = bc.Transaction()
    instance.set_locktime(2143)
    assert instance.is_locktime_conflict()

def transaction__is_locktime_conflict__input_max_sequence__returns_true():
    input = bc.Input()
    input.set_sequence(bc.max_input_sequence)
    instance = bc.Transaction.from_tuple(0, 2143, [input], [])
    assert instance.is_locktime_conflict()

def transaction__from_data__insufficient_version_bytes__failure():
    instance = bc.Transaction.from_data(bytes.fromhex("0000"))
    assert instance is None

def transaction__from_data__insufficient_input_bytes__failure():
    data = bytes.fromhex("0000000103")
    instance = bc.Transaction.from_data(data)
    assert instance is None

def transaction__from_data__insufficient_output_bytes__failure():
    data = bytes.fromhex("000000010003")
    instance = bc.Transaction.from_data(data)
    assert instance is None

def transaction__from_data__compare_wire_to_store__success():
    wire = True
    data_wire = bytes.fromhex(TX3_WIRE_SERIALIZED)

    wire_tx = bc.Transaction.from_data(data_wire, wire)
    assert wire_tx is not None
    assert data_wire == wire_tx.to_data(wire)

    store_text = wire_tx.to_data(not wire).hex()

    data_store = bytes.fromhex(TX3_STORE_SERIALIZED)
    store_tx = bc.Transaction.from_data(data_store, not wire)
    assert store_tx is not None
    assert data_store == store_tx.to_data(not wire)

    assert wire_tx == store_tx

def transaction__factory_data_1__case_1__success():
    tx_hash = bc.hash_literal(TX1_HASH)
    raw_tx = bytes.fromhex(TX1)
    assert len(raw_tx) == 225

    tx = bc.Transaction.from_data(raw_tx)
    assert tx is not None
    assert tx.is_valid()
    assert tx.serialized_size() == 225
    assert tx.hash() == tx_hash

    assert tx.serialized_size() == len(raw_tx)
    resave = tx.to_data()
    assert resave == raw_tx

def transaction__factory_data_1__case_2__success():
    tx_hash = bc.hash_literal(TX4_HASH)
    raw_tx = bytes.fromhex(TX4)
    assert len(raw_tx) == 523

    tx = bc.Transaction.from_data(raw_tx)
    assert tx is not None
    assert tx.is_valid()
    assert tx.hash() == tx_hash

    assert tx.serialized_size() == len(raw_tx)
    resave = tx.to_data()
    assert resave == raw_tx

def transaction__version__roundtrip__success():
    version = 1254
    instance = bc.Transaction()
    assert version != instance.version()
    instance.set_version(version)
    assert version == instance.version()

def transaction__locktime__roundtrip__success():
    locktime = 1254
    instance = bc.Transaction()
    assert locktime != instance.locktime()
    instance.set_locktime(locktime)
    assert locktime == instance.locktime()

def transaction__inputs_setter_1__roundtrip__success():
    input = bc.Input.from_data(bytes.fromhex(TX0))

    instance = bc.Transaction()
    assert [input] != instance.inputs()
    instance.set_inputs([input])
    assert [input] == instance.inputs()

def transaction__outputs_setter_1__roundtrip__success():
    output = bc.Output.from_data(bytes.fromhex(TX0_LAST_OUTPUT))

    instance = bc.Transaction()
    assert [output] != instance.outputs()
    instance.set_outputs([output])
    assert [output] == instance.outputs()

def transaction__is_oversized_coinbase__non_coinbase_tx__returns_false():
    data = bytes.fromhex(TX5)
    instance = bc.Transaction.from_data(data)
    assert instance is not None
    assert not instance.is_coinbase()
    assert not instance.is_oversized_coinbase()

def transaction__is_oversized_coinbase__script_size_below_min__returns_true():
    prevout = bc.OutputPoint()
    prevout.base.set_index(bc.Point.null_index)
    prevout.base.set_hash(bc.null_hash)
    input = bc.Input()
    input.set_previous_output(prevout)
    instance = bc.Transaction()
    instance.set_inputs([input])
    assert instance.is_coinbase()
    assert input.script().serialized_size(False) < bc.min_coinbase_size
    assert instance.is_oversized_coinbase()

def transaction__is_oversized_coinbase__script_size_above_max__returns_true():
    prevout = bc.OutputPoint()
    prevout.base.set_index(bc.Point.null_index)
    prevout.base.set_hash(bc.null_hash)
    input_script = bc.Script.from_data(bytes.fromhex(
        "00" * (bc.max_coinbase_size + 10)), False)
    assert input_script is not None
    input = bc.Input()
    input.set_previous_output(prevout)
    input.set_script(input_script)
    instance = bc.Transaction()
    instance.set_inputs([input])
    assert instance.is_coinbase()
    assert input.script().serialized_size(False) > bc.max_coinbase_size
    assert instance.is_oversized_coinbase()

def transaction__is_oversized_coinbase__script_size_within_bounds__returns_false():
    prevout = bc.OutputPoint()
    prevout.base.set_index(bc.Point.null_index)
    prevout.base.set_hash(bc.null_hash)
    input_script = bc.Script.from_data(bytes.fromhex("00" * 50), False)
    assert input_script is not None
    input = bc.Input()
    input.set_previous_output(prevout)
    input.set_script(input_script)
    instance = bc.Transaction()
    instance.set_inputs([input])
    assert instance.is_coinbase()
    assert input.script().serialized_size(False) >= bc.min_coinbase_size
    assert input.script().serialized_size(False) <= bc.max_coinbase_size
    assert not instance.is_oversized_coinbase()

def transaction__is_null_non_coinbase__coinbase_tx__returns_false():
    data = bytes.fromhex(TX6)
    instance = bc.Transaction.from_data(data)
    assert not instance.is_null_non_coinbase()

def transaction__is_null_non_coinbase__no_null_input_prevout__returns_false():
    instance = bc.Transaction()
    assert not instance.is_coinbase()
    assert not instance.is_null_non_coinbase()

def transaction__is_null_non_coinbase__null_input_prevout__returns_true():
    prevout = bc.OutputPoint()
    prevout.base.set_index(bc.Point.null_index)
    prevout.base.set_hash(bc.null_hash)
    input0 = bc.Input()
    input1 = bc.Input()
    input1.set_previous_output(prevout)
    instance = bc.Transaction()
    instance.set_inputs([input0, input1])
    assert not instance.is_coinbase()
    assert prevout.is_null()
    assert instance.is_null_non_coinbase()

def transaction__total_input_value__no_cache__returns_zero():
    input = bc.Input()
    instance = bc.Transaction()
    instance.set_inputs([input, input])
    assert instance.total_input_value() == 0

def transaction__total_input_value__cache__returns_cache_value_sum():
    instance = bc.Transaction()
    input0 = bc.Input()
    input1 = bc.Input()
    input0.previous_output().validation.cache.set_value(123)
    input1.previous_output().validation.cache.set_value(123)
    instance.set_inputs([input0, input1])
    assert instance.total_input_value() == 444

def transaction__total_output_value__empty_outputs__returns_zero():
    instance = bc.Transaction()
    assert instance.total_output_value() == 0

def transaction__total_output_value__non_empty_outputs__returns_sum():
    instance = bc.Transaction()

    output0 = bc.Output()
    output0.set_value(1200)
    output1 = bc.Output()
    output1.set_value(34)
    instance.set_outputs([output0, output1])
    assert instance.total_output_value() == 1234

def transaction__fees__nonempty__returns_outputs_minus_inputs():
    instance = bc.Transaction()
    input0 = bc.Input()
    input1 = bc.Input()
    input0.previous_output().validation.cache.set_value(123)
    input1.previous_output().validation.cache.set_value(321)
    instance.set_inputs([input0, input1])
    output0 = bc.Output()
    output0.set_value(44)
    instance.set_outputs([output0])
    assert instance.fees() == 400

def transaction__is_overspent__output_does_not_exceed_input__returns_false():
    instance = bc.Transaction()
    assert not instance.is_overspent()

def transaction__is_overspent__output_exceeds_input__returns_true():
    instance = bc.Transaction()

    output0 = bc.Output()
    output0.set_value(1200)
    output1 = bc.Output()
    output1.set_value(34)
    instance.set_outputs([output0, output1])
    assert instance.is_overspent()

# TODO: tests with initialized data
def transaction__signature_operations_single_input_output_uninitialized__returns_zero():
    instance = bc.Transaction()
    instance.set_inputs([bc.Input()])
    instance.set_outputs([bc.Output()])
    assert instance.signature_operations(False) == 0

def transaction__is_missing_previous_outputs__empty_inputs__returns_false():
    instance = bc.Transaction()
    assert not instance.is_missing_previous_outputs()

def transaction__is_missing_previous_outputs__inputs_without_cache_value__returns_true():
    instance = bc.Transaction()
    instance.set_inputs([bc.Input()])
    assert instance.is_missing_previous_outputs()

def transaction__is_missing_previous_outputs__inputs_with_cache_value__returns_false():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.cache.set_value(123)
    instance.set_inputs([input])
    assert not instance.is_missing_previous_outputs()

def transaction__missing_previous_outputs__empty_inputs__returns_empty():
    instance = bc.Transaction()
    assert len(instance.missing_previous_outputs()) == 0

def transaction__missing_previous_outputs__inputs_without_cache_value__returns_single_index():
    instance = bc.Transaction()
    input = bc.Input()
    instance.set_inputs([input])
    result = instance.missing_previous_outputs()
    assert len(result) == 1
    assert result[-1] == 0

def transaction__missing_previous_outputs__inputs_with_cache_value__returns_empty():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.cache.set_value(123)
    instance.set_inputs([input])
    assert not instance.missing_previous_outputs()

def transaction__is_double_spend__empty_inputs__returns_false():
    instance = bc.Transaction()
    assert not instance.is_double_spend(False)
    assert not instance.is_double_spend(True)

def transaction__is_double_spend__unspent_inputs__returns_false():
    instance = bc.Transaction()
    input = bc.Input()
    instance.set_inputs([input])
    assert not instance.is_double_spend(False)
    assert not instance.is_double_spend(True)

def transaction__is_double_spend__include_unconfirmed_false_with_unconfirmed__returns_false():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.spent = True
    instance.set_inputs([input])
    assert not instance.is_double_spend(False)

def transaction__is_double_spend__include_unconfirmed_false_with_confirmed__returns_true():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.spent = True
    input.previous_output().validation.confirmed = True
    instance.set_inputs([input])
    assert instance.is_double_spend(False)

def transaction__is_double_spend__include_unconfirmed_true_with_unconfirmed__returns_true():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.spent = True
    instance.set_inputs([input])
    assert instance.is_double_spend(True)

def transaction__double_spends__empty_inputs__returns_empty():
    instance = bc.Transaction()
    assert not instance.double_spends(False)
    assert not instance.double_spends(True)

def transaction__double_spends__unspent_inputs__returns_empty():
    instance = bc.Transaction()
    instance.set_inputs([bc.Input()])
    assert not instance.double_spends(False)
    assert not instance.double_spends(True)

def transaction__double_spends__include_unconfirmed_false_with_unconfirmed__returns_empty():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.spent = True
    instance.set_inputs([input])
    assert not instance.double_spends(False)

def transaction__double_spends__include_unconfirmed_false_with_confirmed__returns_expected():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.spent = True
    input.previous_output().validation.confirmed = True
    instance.set_inputs([input])
    result = instance.double_spends(False)
    assert len(result) == 1
    assert result[-1] == 0

def transaction__double_spends__include_unconfirmed_true_with_unconfirmed__returns_expected():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.spent = True
    instance.set_inputs([input])
    result = instance.double_spends(True)
    assert len(result) == 1
    assert result[-1] == 0

def transaction__is_immature__empty_inputs__returns_false():
    instance = bc.Transaction()
    assert not instance.is_immature(453)

def transaction__is_immature__mature_inputs__returns_false():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().base.set_index(123)
    instance.set_inputs([input])
    assert not instance.is_immature(453)

def transaction__is_immature__immature_inputs__returns_true():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.height = 20
    instance.set_inputs([input])
    assert instance.is_immature(50)

def transaction__immature_inputs__empty_inputs__returns_empty():
    instance = bc.Transaction()
    assert not instance.immature_inputs(453)

def transaction__immature_inputs__mature_inputs__returns_empty():
    input = bc.Input()
    input.previous_output().base.set_index(123)
    instance = bc.Transaction()
    instance.set_inputs([input])
    assert not instance.immature_inputs(453)

def transaction__immature_inputs__immature_inputs__returns_input_indexes():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output().validation.height = 20
    instance.set_inputs([input])
    result = instance.immature_inputs(50)
    assert len(result) == 1
    assert result[-1] == 0

def transaction__operator_assign_equals_1__always__matches_equivalent():
    raw_tx = bytes.fromhex(TX4)
    expected = bc.Transaction.from_data(raw_tx)
    assert expected is not None
    instance = bc.Transaction.from_data(raw_tx)
    assert instance == expected

def transaction__operator_boolean_equals__duplicates__returns_true():
    raw_tx = bytes.fromhex(TX4)
    alpha = bc.Transaction.from_data(raw_tx)
    assert alpha is not None
    beta = bc.Transaction.from_data(raw_tx)
    assert beta is not None
    assert alpha == beta

def transaction__operator_boolean_equals__differs__returns_false():
    raw_tx = bytes.fromhex(TX4)
    alpha = bc.Transaction.from_data(raw_tx)
    assert alpha is not None
    beta = bc.Transaction()
    assert beta is not None
    assert alpha != beta

def transaction__hash__block320670__success():
    expected = bc.hash_literal(TX7_HASH)
    data = bytes.fromhex(TX7)
    instance = bc.Transaction.from_data(data)
    assert instance is not None
    assert expected == instance.hash()
    assert data == instance.to_data()

transaction__constructor_1__always__returns_default_initialized()
transaction__constructor_2__valid_input__returns_input_initialized()
transaction__constructor_4__valid_input__returns_input_initialized()
transaction__constructor_6__valid_input__returns_input_initialized()
transaction__is_coinbase__empty_inputs__returns_false()
transaction__is_coinbase__with_coinbase_input__returns_true()
transaction__is_final__locktime_zero__returns_true()
transaction__is_final__locktime_less_block_time_greater_threshold__returns_true()
transaction__is_final__locktime_less_block_height_less_threshold_returns_true()
transaction__is_final__locktime_input_not_final__returns_false()
transaction__is_final__locktime_inputs_final__returns_true()
transaction__is_locktime_conflict__locktime_zero__returns_false()
transaction__is_locktime_conflict__input_sequence_not_maximum__returns_false()
transaction__is_locktime_conflict__no_inputs__returns_true()
transaction__is_locktime_conflict__input_max_sequence__returns_true()
transaction__from_data__insufficient_version_bytes__failure()
transaction__from_data__insufficient_input_bytes__failure()
transaction__from_data__insufficient_output_bytes__failure()
transaction__from_data__compare_wire_to_store__success()
transaction__factory_data_1__case_1__success()
transaction__factory_data_1__case_2__success()
transaction__version__roundtrip__success()
transaction__locktime__roundtrip__success()
transaction__inputs_setter_1__roundtrip__success()
transaction__outputs_setter_1__roundtrip__success()
transaction__is_oversized_coinbase__non_coinbase_tx__returns_false()
transaction__is_oversized_coinbase__script_size_below_min__returns_true()
transaction__is_oversized_coinbase__script_size_above_max__returns_true()
transaction__is_oversized_coinbase__script_size_within_bounds__returns_false()
transaction__is_null_non_coinbase__coinbase_tx__returns_false()
transaction__is_null_non_coinbase__no_null_input_prevout__returns_false()
transaction__total_input_value__no_cache__returns_zero()
transaction__total_output_value__empty_outputs__returns_zero()
transaction__total_output_value__non_empty_outputs__returns_sum()
transaction__fees__nonempty__returns_outputs_minus_inputs()
transaction__is_overspent__output_does_not_exceed_input__returns_false()
transaction__is_overspent__output_exceeds_input__returns_true()
transaction__signature_operations_single_input_output_uninitialized__returns_zero()
transaction__is_missing_previous_outputs__empty_inputs__returns_false()
transaction__is_missing_previous_outputs__inputs_without_cache_value__returns_true()
transaction__is_missing_previous_outputs__inputs_with_cache_value__returns_false()
transaction__missing_previous_outputs__empty_inputs__returns_empty()
transaction__missing_previous_outputs__inputs_without_cache_value__returns_single_index()
transaction__missing_previous_outputs__inputs_with_cache_value__returns_empty()
transaction__is_double_spend__empty_inputs__returns_false()
transaction__is_double_spend__unspent_inputs__returns_false()
transaction__is_double_spend__include_unconfirmed_false_with_unconfirmed__returns_false()
transaction__is_double_spend__include_unconfirmed_false_with_confirmed__returns_true()
transaction__is_double_spend__include_unconfirmed_true_with_unconfirmed__returns_true()
transaction__double_spends__empty_inputs__returns_empty()
transaction__double_spends__unspent_inputs__returns_empty()
transaction__double_spends__include_unconfirmed_false_with_unconfirmed__returns_empty()
transaction__double_spends__include_unconfirmed_false_with_confirmed__returns_expected()
transaction__double_spends__include_unconfirmed_true_with_unconfirmed__returns_expected()
transaction__is_immature__empty_inputs__returns_false()
transaction__is_immature__mature_inputs__returns_false()
transaction__is_immature__immature_inputs__returns_true()
transaction__immature_inputs__empty_inputs__returns_empty()
transaction__immature_inputs__mature_inputs__returns_empty()
transaction__immature_inputs__immature_inputs__returns_input_indexes()
transaction__operator_assign_equals_1__always__matches_equivalent()
transaction__operator_boolean_equals__duplicates__returns_true()
transaction__operator_boolean_equals__differs__returns_false()
transaction__hash__block320670__success()

