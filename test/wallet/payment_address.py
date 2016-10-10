from libbitcoin import bc

# $ bx base16-encode "Satoshi" | bx sha256
SECRET = "002688cc350a5333a87fa622eacec626c3d1c0ebf9f3793de3885fa254d7e393"
SCRIPT = "dup hash160 [ 18c0bd8d1818f1bf99cb1df2269c645318ef7b73 ] equalverify checksig"

# $ bx base16-encode "Satoshi" | bx sha256 | bx ec-to-public
COMPRESSED = "03d24123978d696a6c964f2dcb1d1e000d4150102fbbcc37f020401e35fb4cb745"
# $ bx base16-encode "Satoshi" | bx sha256 | bx ec-to-public -u
UNCOMPRESSED = "04d24123978d696a6c964f2dcb1d1e000d4150102fbbcc37f020401e35fb4cb74561a3362716303b0469f04c3d0e3cbc4b5b62a2da7add6ecc3b254404b12d2f83"

# $ bx base16-encode "Satoshi" | bx sha256 | bx ec-to-public | bx bitcoin160
COMPRESSED_HASH = "f85beb6356d0813ddb0dbb14230a249fe931a135"
# $ bx base16-encode "Satoshi" | bx sha256 | bx ec-to-public -u | bx bitcoin160
UNCOMPRESSED_HASH = "96ec4e06c665b7bd62cbe3d232f7c2d34016e136"

# $ bx base16-encode "Satoshi" | bx sha256 | bx ec-to-public | bx ec-to-address
ADDRESS_COMPRESSED = "1PeChFbhxDD9NLbU21DfD55aQBC4ZTR3tE"
# $ bx base16-encode "Satoshi" | bx sha256 | bx ec-to-public -u | bx ec-to-address
ADDRESS_UNCOMPRESSED = "1Em1SX7qQq1pTmByqLRafhL1ypx2V786tP"

# $ bx base16-encode "Satoshi" | bx sha256 | bx ec-to-public | bx ec-to-address -v 111
ADDRESS_COMPRESSED_TESTNET = "n4A9zJggmEeQ9T55jaC32zHuGAnmSzPU2L"
# $ bx script-encode "dup hash160 [ 18c0bd8d1818f1bf99cb1df2269c645318ef7b73 ] equalverify checksig"
ADDRESS_UNCOMPRESSED_TESTNET = "muGxjaCpDrT5EsfbYuPxVcYLqpYjNQnbkR"

# $ bx script-to-address "dup hash160 [ 18c0bd8d1818f1bf99cb1df2269c645318ef7b73 ] equalverify checksig"
ADDRESS_SCRIPT = "3CPSWnCGjkePffNyVptkv45Bx35SaAwm7d"
# $ bx script-to-address "dup hash160 [ 18c0bd8d1818f1bf99cb1df2269c645318ef7b73 ] equalverify checksig" -v 196
ADDRESS_SCRIPT_TESTNET = "2N3weaX8JMD9jsT1XAxWdY14TAPHcKYKHCT"

# $ bx script-to-address "dup hash160 [ 18c0bd8d1818f1bf99cb1df2269c645318ef7b73 ] equalverify checksig" | bx base58-decode
PAYMENT = "0575566c599452b7bcb7f8cd4087bde9686fa9c52d8c2a7d90"
# $ bx script-to-address "dup hash160 [ 18c0bd8d1818f1bf99cb1df2269c645318ef7b73 ] equalverify checksig" -v 196 | bx base58-decode
PAYMENT_TESTNET = "c475566c599452b7bcb7f8cd4087bde9686fa9c52d2fba2898"

# $ bx base58-decode 1111111111111111111114oLvT2 | bx wrap-decode
# wrapper
# {
#     checksum 285843604
#     payload 0000000000000000000000000000000000000000
#     version 0
# }
UNINITIALIZED_ADDRESS = "1111111111111111111114oLvT2"

# negative tests:

def payment_address__construct__default__invalid():
    address = bc.PaymentAddress()
    assert not address.is_valid()
    assert str(address) == UNINITIALIZED_ADDRESS

def payment_address__construct__string_invalid__invalid():
    address = bc.PaymentAddress("bogus")
    assert not address.is_valid()
    assert str(address) == UNINITIALIZED_ADDRESS

# construct secret:

def payment_address__construct__secret__valid_expected():
    secret = bc.EcSecret.from_string(SECRET)
    address = bc.PaymentAddress.from_secret(secret)
    assert address.is_valid()
    assert str(address) == ADDRESS_COMPRESSED

payment_address__construct__default__invalid()
payment_address__construct__string_invalid__invalid()
payment_address__construct__secret__valid_expected()

