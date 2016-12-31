from libbitcoin import bc

# Scenario 1
SECRET1 = "8010b1bb119ad37d4b65a1022a314897b1b3614b345974332cb1b9582cf03536"
COMPRESSED1 = "0309ba8621aefd3b6ba4ca6d11a4746e8df8d35d9b51b383338f627ba7fc732731"
UNCOMPRESSED1 = "0409ba8621aefd3b6ba4ca6d11a4746e8df8d35d9b51b383338f627ba7fc7327318c3a6ec6acd33c36328b8fb4349b31671bcd3a192316ea4f6236ee1ae4a7d8c9"

# Scenario 2
COMPRESSED2 = "03bc88a1bd6ebac38e9a9ed58eda735352ad10650e235499b7318315cc26c9b55b"
SIGHASH2 = "ed8f9b40c2d349c8a7e58cebe79faa25c21b6bb85b874901f72a1b3f1ad0a67f"
SIGNATURE2 = "3045022100bc494fbd09a8e77d8266e2abdea9aef08b9e71b451c7d8de9f63cda33a62437802206b93edd6af7c659db42c579eb34a3a4cb60c28b5a6bc86fd5266d42f6b8bb67d"

# Scenario 3
SECRET3 = "ce8f4b713ffdd2658900845251890f30371856be201cd1f5b3d970f793634333"
SIGHASH3 = "f89572635651b2e4f89778350616989183c98d1a721c911324bf9f17a0cf5bf0"
EC_SIGNATURE3 = "4832febef8b31c7c922a15cb4063a43ab69b099bba765e24facef50dfbb4d057928ed5c6b6886562c2fe6972fd7c7f462e557129067542cce6b37d72e5ea5037"
DER_SIGNATURE3 = "3044022057d0b4fb0df5cefa245e76ba9b099bb63aa46340cb152a927c1cb3f8befe324802203750eae5727db3e6cc4275062971552e467f7cfd7269fec2626588b6c6d58e92"

def elliptic_curve__secret_to_public__positive__test():
    secret1 = bc.EcSecret.from_bytes(bytes.fromhex(SECRET1))
    point = secret1.to_public()
    assert point is not None
    assert point.encode_base16() == COMPRESSED1

def elliptic_curve__decompress__positive__test():
    compressed = bc.EcCompressed.from_string(COMPRESSED1)
    uncompressed = compressed.decompress()
    assert uncompressed is not None
    assert uncompressed.encode_base16() == UNCOMPRESSED1

def elliptic_curve__sign__positive__test():
    secret = bc.EcSecret.from_string(SECRET3, True)
    sighash = bc.HashDigest.from_string(SIGHASH3, True)
    signature = secret.sign(sighash)
    assert signature is not None
    assert signature.hex() == EC_SIGNATURE3

def elliptic_curve__encode_signature__positive__test():
    signature = bc.EcSignature.from_string(EC_SIGNATURE3)
    out = signature.encode()
    assert out is not None
    assert out.hex() == DER_SIGNATURE3

def elliptic_curve__sign__round_trip_positive__test():
    data = b"data"
    hash_ = bc.bitcoin_hash(data)
    secret = bc.EcSecret.from_string(SECRET1, True)
    point = secret.to_public()
    assert point is not None
    signature = secret.sign(hash_)
    assert signature is not None
    assert point.verify(hash_, signature)

def elliptic_curve__sign__round_trip_negative__test():
    data = b"data"
    hash_ = bc.bitcoin_hash(data)
    secret = bc.EcSecret.from_string(SECRET1, True)
    point = secret.to_public()
    assert point is not None
    signature = secret.sign(hash_)
    assert signature is not None

    # Invalidate the positive test.
    hash_ = bc.HashDigest.from_bytes(b"\x00" + hash_.data[1:])
    assert not point.verify(hash_, signature)

def elliptic_curve__verify_signature__positive__test():
    strict = False
    sighash = bc.HashDigest.from_string(SIGHASH2, True)
    point = bc.EcCompressed.from_string(COMPRESSED2)
    distinguished = bytes.fromhex(SIGNATURE2)
    signature = bc.EcSignature.from_der(distinguished, strict)
    assert signature is not None
    assert point.verify(sighash, signature)

def elliptic_curve__verify_signature__negative__test():
    strict = False
    sighash = bc.HashDigest.from_string(SIGHASH2, True)
    point = bc.EcCompressed.from_string(COMPRESSED2)
    distinguished = bytes.fromhex(SIGNATURE2)
    signature = bc.EcSignature.from_der(distinguished, strict)
    assert signature is not None

    # Invalidate the positive test.
    signature = bc.EcSignature.from_bytes(
        signature.data[0:10] + b"N" + signature.data[10:])
    assert not point.verify(sighash, signature)

def elliptic_curve__ec_add__positive__test():
    zero_padding = [0] * (bc.EcSecret.size - 3)
    secret1 = bc.EcSecret.from_bytes(bytes([1, 2, 3] + zero_padding))
    secret2 = bc.EcSecret.from_bytes(bytes([3, 2, 1] + zero_padding))
    public1 = secret1.to_public()
    assert public1 is not None
    secret1 += secret2
    assert secret1.encode_base16() == "0404040000000000000000000000000000000000000000000000000000000000"

    public2 = secret1.to_public()
    public1 += secret2
    assert public1 == public2

def elliptic_curve__ec_add__negative__test():
    # = n - 1
    secret1 = bc.EcSecret.from_string("fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140");
    zero_padding = [0] * (bc.EcSecret.size - 1)
    secret2 = bc.EcSecret.from_bytes(bytes(zero_padding + [1]))
    public1 = secret1.to_public()
    secret1 += secret2
    assert secret1 is None
    public1 += secret2
    assert public1 is None

def elliptic_curve__ec_multiply_test():
    zero_padding = [0] * (bc.EcSecret.size - 1)
    secret1 = bc.EcSecret.from_bytes(bytes(zero_padding + [11]))
    secret2 = bc.EcSecret.from_bytes(bytes(zero_padding + [22]))
    public1 = secret1.to_public()
    assert public1 is not None
    secret1 *= secret2
    assert secret1 is not None
    assert secret1.data[31] == 242
    public1 *= secret2

    public2 = secret1.to_public()
    assert public1 == public2

elliptic_curve__secret_to_public__positive__test()
elliptic_curve__decompress__positive__test()
elliptic_curve__sign__positive__test()
elliptic_curve__encode_signature__positive__test()
elliptic_curve__sign__round_trip_positive__test()
elliptic_curve__sign__round_trip_negative__test()
elliptic_curve__verify_signature__positive__test()
elliptic_curve__verify_signature__negative__test()
elliptic_curve__ec_add__positive__test()
elliptic_curve__ec_add__negative__test()
elliptic_curve__ec_multiply_test()

