from libbitcoin import bc

def is_coinbase_returns_false():
    instance = bc.Transaction()
    assert not instance.is_coinbase()

def is_coinbase_returns_true():
    instance = bc.Transaction()
    inputs = instance.copy_inputs()
    input = bc.Input()
    prevout = bc.OutputPoint.from_tuple(bc.null_hash, bc.max_input_sequence)
    input.set_previous_output(prevout)
    inputs.append(input)
    instance.set_inputs(inputs)
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
    inputs = instance.copy_inputs()
    input = bc.Input()
    input.sequence = 1
    inputs.append(input)
    instance.set_inputs(inputs)
    assert not instance.is_final(height, time)

def is_final_locktime_inputs_final_returns_true():
    height = 100
    time = 100
    instance = bc.Transaction()
    instance.locktime = 101
    inputs = instance.copy_inputs()
    input = bc.Input()
    input.sequence = bc.max_input_sequence
    inputs.append(input)
    instance.set_inputs(inputs)
    assert instance.is_final(height, time)

def is_locktime_conflict_locktime_zero_returns_false():
    instance = bc.Transaction()
    instance.locktime = 0
    assert not instance.is_locktime_conflict()

def is_locktime_conflict_input_sequence_not_maximum_returns_false():
    instance = bc.Transaction()
    instance.locktime = 2143
    inputs = instance.copy_inputs()
    input = bc.Input()
    input.sequence = 1
    inputs.append(input)
    instance.set_inputs(inputs)
    assert not instance.is_locktime_conflict()

is_coinbase_returns_false()
is_coinbase_returns_true()
is_final_locktime_zero_returns_true()
is_final_locktime_less_block_time_greater_threshold_returns_true()
is_final_locktime_less_block_height_less_threshold_returns_true()
is_final_locktime_input_not_final_returns_false()
is_final_locktime_inputs_final_returns_true()
is_locktime_conflict_locktime_zero_returns_false()
is_locktime_conflict_input_sequence_not_maximum_returns_false()

