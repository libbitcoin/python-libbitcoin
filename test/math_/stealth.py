from libbitcoin import bc

SCAN_PRIVATE = "fa63521e333e4b9f6a98a142680d3aef4d8e7f79723ce0043691db55c36bd905"
SCAN_PUBLIC = "034ea70b28d607bf3a2493102001cab35689cf2152530bf8bf8a5b594af6ae31d0"

SPEND_PRIVATE = "dcc1250b51c0f03ae4e978e0256ede51dc1144e345c926262b9717b1bcc9bd1b"
SPEND_PUBLIC = "03d5b3853bbee336b551ff999b0b1d656e65a7649037ae0dcb02b3c4ff5f29e5be"

EPHEMERAL_PRIVATE = "5f70a77b32260a7a32c62242381fba2cf40c0e209e665a7959418eae4f2da22b"
EPHEMERAL_PUBLIC = "0387ff9128d18ddcec0a8119589a62b88bc035cb9cd6db08ce5ff702a78ef8f922"

STEALTH_PRIVATE = "280a9931c0a7b8f9bed96bad35f69a1431817fb77043fdff641ad48ce1e4411e"
STEALTH_PUBLIC = "0305f6b99a44a2bdec8b484ffcee561cf9a0c3b7ea92ea8e6334e6fbc4f1c17899"

# $ bx ec-add 03d5b3853bbee336b551ff999b0b1d656e65a7649037ae0dcb02b3c4ff5f29e5be 4b4974266ee6c8bed9eff2cd1087bbc1101f17bad9c37814f8561b67f550c544 | bx ec-to-address
P2PKH_ADDRESS = "1Gvq8pSTRocNLDyf858o4PL3yhZm5qQDgB"

# $ bx ec-add 03d5b3853bbee336b551ff999b0b1d656e65a7649037ae0dcb02b3c4ff5f29e5be 4b4974266ee6c8bed9eff2cd1087bbc1101f17bad9c37814f8561b67f550c544 | bx ec-to-address - v 111
P2PKH_ADDRESS_TESTNET = "mwSnRsXSEq3d7LTGqe7AtJYNqhATwHdhMb"

def stealth_round_trip():
    expected_stealth_private = bc.EcSecret.from_bytes(
        bytes.fromhex(STEALTH_PRIVATE))

    # Receiver generates a new scan private.
    scan_private = bc.EcSecret.from_bytes(bytes.fromhex(SCAN_PRIVATE))
    scan_public = scan_private.to_public()
    assert scan_public.data.hex() == SCAN_PUBLIC

    # Receiver generates a new spend private.
    spend_private = bc.EcSecret.from_bytes(bytes.fromhex(SPEND_PRIVATE))
    spend_public = spend_private.to_public()
    assert spend_public.data.hex() == SPEND_PUBLIC

    # Sender generates a new ephemeral key.
    ephemeral_private = bc.EcSecret.from_bytes(
        bytes.fromhex(EPHEMERAL_PRIVATE))
    ephemeral_public = ephemeral_private.to_public()
    assert ephemeral_public.data.hex() == EPHEMERAL_PUBLIC

    # Sender derives stealth public, requiring ephemeral private.
    sender_public = bc.uncover_stealth(scan_public, ephemeral_private,
                                       spend_public)
    assert sender_public.data.hex() == STEALTH_PUBLIC

    # Receiver derives stealth public, requiring scan private.
    receiver_public = bc.uncover_stealth(ephemeral_public, scan_private,
                                         spend_public)
    assert receiver_public.data.hex()

    # Only reciever can derive stealth private, as it requires both scan
    # and spend private.
    stealth_private = bc.uncover_stealth(ephemeral_public, scan_private,
                                         spend_private)

    # This shows that both parties have actually generated stealth public.
    stealth_public = stealth_private.to_public()
    assert stealth_public.data.hex() == STEALTH_PUBLIC

    # Both parties therefore have the ability to generate the p2pkh address.
    # versioning: stealth_address::main corresponds to payment_address::main_p2pkh
    public = bc.EcPublic.from_compressed(stealth_public)
    address = bc.PaymentAddress.from_point(public,
                                           bc.PaymentAddress.mainnet_p2kh)
    assert str(address) == P2PKH_ADDRESS

stealth_round_trip()
