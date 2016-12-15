from libbitcoin import bc

def is_coinbase_returns_false():
    instance = bc.Transaction()
    assert not instance.is_coinbase()

def is_coinbase_returns_true():
    instance = bc.Transaction()
    input = bc.Input()
    input.previous_output = bc.OutputPoint.from_tuple(bc.null_hash,
                                                      bc.max_input_sequence)
    instance.set_inputs([input])
    assert instance.is_coinbase()

def is_final_locktime_zero_returns_true():
    height = 100
    time = 100
    instance = bc.Transaction()
    instance.locktime = 0
    assert instance.is_final(height, time)

def is_final_locktime_less_block_time_greater_threshold_returns_true():
    height = bc.locktime_threshold + 100
    time = 100
    instance = bc.Transaction()
    instance.locktime = bc.locktime_threshold + 50
    assert instance.is_final(height, time)

def is_final_locktime_less_block_height_less_threshold_returns_true():
    height = 100
    time = 100
    instance = bc.Transaction()
    instance.locktime = 50
    assert instance.is_final(height, time)

def is_final_locktime_input_not_final_returns_false():
    height = 100
    time = 100
    instance = bc.Transaction()
    instance.locktime = 101
    input = bc.Input()
    input.sequence = 1
    instance.set_inputs([input])
    assert not instance.is_final(height, time)

def is_final_locktime_inputs_final_returns_true():
    height = 100
    time = 100
    instance = bc.Transaction()
    instance.locktime = 101
    input = bc.Input()
    input.sequence = bc.max_input_sequence
    instance.set_inputs([input])
    assert instance.is_final(height, time)

def is_locktime_conflict_locktime_zero_returns_false():
    instance = bc.Transaction()
    instance.locktime = 0
    assert not instance.is_locktime_conflict()

def is_locktime_conflict_input_sequence_not_maximum_returns_false():
    instance = bc.Transaction()
    instance.locktime = 2143
    input = bc.Input()
    input.sequence = 1
    instance.set_inputs([input])
    assert not instance.is_locktime_conflict()

def is_locktime_conflict_no_inputs_returns_true():
    instance = bc.Transaction()
    instance.locktime = 2143
    assert instance.is_locktime_conflict()

def is_locktime_conflict_input_max_sequence_returns_true():
    instance = bc.Transaction()
    instance.locktime = 2143
    input = bc.Input()
    input.sequence = bc.max_input_sequence
    instance.set_inputs([input])
    assert instance.is_locktime_conflict()

def total_output_value_returns_zero():
    instance = bc.Transaction()
    assert instance.total_output_value() == 0

def total_output_value_returns_positive():
    expected = 1234
    instance = bc.Transaction()

    outputs = []
    output = bc.Output()
    output.value = 1200
    outputs.append(output)

    output = bc.Output()
    output.value = 34
    outputs.append(output)

    instance.set_outputs(outputs)
    assert instance.total_output_value() == expected

def from_data_fails():
    data = b"xy"
    instance = bc.Transaction.from_data(data)
    assert not instance.is_valid()

def case_1_factory_data_chunk():
    tx_hash = bc.HashDigest.from_string("bf7c3f5a69a78edd81f3eff7e93a37fb2d7da394d48db4d85e7e5353b9b8e270", True)
    raw_tx = bytes.fromhex(
        "0100000001f08e44a96bfb5ae63eda1a6620adae37ee37ee4777fb0336e1bbbc"
        "4de65310fc010000006a473044022050d8368cacf9bf1b8fb1f7cfd9aff63294"
        "789eb1760139e7ef41f083726dadc4022067796354aba8f2e02363c5e510aa7e"
        "2830b115472fb31de67d16972867f13945012103e589480b2f746381fca01a9b"
        "12c517b7a482a203c8b2742985da0ac72cc078f2ffffffff02f0c9c467000000"
        "001976a914d9d78e26df4e4601cf9b26d09c7b280ee764469f88ac80c4600f00"
        "0000001976a9141ee32412020a324b93b1a1acfdfff6ab9ca8fac288ac000000"
        "00")
    assert len(raw_tx) == 225

    tx = bc.Transaction.from_data(raw_tx)
    assert tx.is_valid()
    assert tx.serialized_size() == 225
    assert tx.hash() == tx_hash

    # Re-save tx and compare against original.
    assert tx.serialized_size() == len(raw_tx)
    resave = tx.to_data()
    assert resave == raw_tx

def case_2_factory_data_chunk():
    tx_hash = bc.HashDigest.from_string("8a6d9302fbe24f0ec756a94ecfc837eaffe16c43d1e68c62dfe980d99eea556f", True)
    raw_tx = bytes.fromhex(
        "010000000364e62ad837f29617bafeae951776e7a6b3019b2da37827921548d1"
        "a5efcf9e5c010000006b48304502204df0dc9b7f61fbb2e4c8b0e09f3426d625"
        "a0191e56c48c338df3214555180eaf022100f21ac1f632201154f3c69e1eadb5"
        "9901a34c40f1127e96adc31fac6ae6b11fb4012103893d5a06201d5cf61400e9"
        "6fa4a7514fc12ab45166ace618d68b8066c9c585f9ffffffff54b755c39207d4"
        "43fd96a8d12c94446a1c6f66e39c95e894c23418d7501f681b010000006b4830"
        "4502203267910f55f2297360198fff57a3631be850965344370f732950b47795"
        "737875022100f7da90b82d24e6e957264b17d3e5042bab8946ee5fc676d15d91"
        "5da450151d36012103893d5a06201d5cf61400e96fa4a7514fc12ab45166ace6"
        "18d68b8066c9c585f9ffffffff0aa14d394a1f0eaf0c4496537f8ab9246d9663"
        "e26acb5f308fccc734b748cc9c010000006c493046022100d64ace8ec2d5feeb"
        "3e868e82b894202db8cb683c414d806b343d02b7ac679de7022100a2dcd39940"
        "dd28d4e22cce417a0829c1b516c471a3d64d11f2c5d754108bdc0b012103893d"
        "5a06201d5cf61400e96fa4a7514fc12ab45166ace618d68b8066c9c585f9ffff"
        "ffff02c0e1e400000000001976a914884c09d7e1f6420976c40e040c30b2b622"
        "10c3d488ac20300500000000001976a914905f933de850988603aafeeb2fd7fc"
        "e61e66fe5d88ac00000000")
    assert len(raw_tx) == 523

    tx = bc.Transaction.from_data(raw_tx)
    assert tx.is_valid()
    assert tx.hash() == tx_hash

    # Re-save tx and compare against original.
    assert tx.serialized_size() == len(raw_tx)
    resave = tx.to_data()
    assert resave == raw_tx

is_coinbase_returns_false()
is_coinbase_returns_true()
is_final_locktime_zero_returns_true()
is_final_locktime_less_block_time_greater_threshold_returns_true()
is_final_locktime_less_block_height_less_threshold_returns_true()
is_final_locktime_input_not_final_returns_false()
is_final_locktime_inputs_final_returns_true()
is_locktime_conflict_locktime_zero_returns_false()
is_locktime_conflict_input_sequence_not_maximum_returns_false()
is_locktime_conflict_no_inputs_returns_true()
is_locktime_conflict_input_max_sequence_returns_true()
total_output_value_returns_zero()
total_output_value_returns_positive()
from_data_fails()
case_1_factory_data_chunk()
case_2_factory_data_chunk()

