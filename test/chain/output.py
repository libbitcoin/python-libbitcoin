from libbitcoin import bc

valid_raw_output = bytes.fromhex(
    "20300500000000001976a914905f933de850988603aafeeb2fd7fce61e66fe5d88ac")

def from_data_fails():
    data = b"0" * 2

    instance = bc.Output.from_data(data)
    assert not instance.is_valid()

def factory_data_chunk_success():
    instance = bc.Output.from_data(valid_raw_output)
    assert instance.is_valid()
    assert instance.serialized_size() == len(valid_raw_output)

    # Re-save and compare against original.
    resave = instance.to_data()
    assert resave == valid_raw_output

from_data_fails()
factory_data_chunk_success()

