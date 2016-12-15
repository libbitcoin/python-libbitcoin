from libbitcoin import bc

def from_data_fails():
    data = b"0" * 10
    header = bc.Header.from_data(data)
    assert not header.is_valid()

def roundtrip_to_data_factory_from_data_chunk():
    expected = bc.Header.from_tuple([
        10,
        bc.HashDigest.from_string("000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f", True),
        bc.HashDigest.from_string("4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b", True),
        531234,
        6523454,
        68644
    ])

    data = expected.to_data()

    result = bc.Header.from_data(data)

    assert result.is_valid()
    assert expected == result

from_data_fails()
roundtrip_to_data_factory_from_data_chunk()

