from libbitcoin import bc

valid_raw_input = bytes.fromhex(
    "54b755c39207d443fd96a8d12c94446a1c6f66e39c95e894c23418d7501f681b01000"
    "0006b48304502203267910f55f2297360198fff57a3631be850965344370f732950b4"
    "7795737875022100f7da90b82d24e6e957264b17d3e5042bab8946ee5fc676d15d915"
    "da450151d36012103893d5a06201d5cf61400e96fa4a7514fc12ab45166ace618d68b"
    "8066c9c585f9ffffffff")

def from_data_fails():
    data = b"0" * 2
    instance = bc.Input.from_data(data)
    assert not instance.is_valid()

def factory_data_chunk_success():
    instance = bc.Input.from_data(valid_raw_input)
    assert instance.is_valid()
    assert instance.serialized_size() == len(valid_raw_input)

    # Re-save and compare against original.
    resave = instance.to_data()
    assert resave == valid_raw_input

from_data_fails()
factory_data_chunk_success()

