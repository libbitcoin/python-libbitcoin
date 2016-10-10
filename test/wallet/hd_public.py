from libbitcoin import bc

SHORT_SEED = "000102030405060708090a0b0c0d0e0f"
LONG_SEED = "fffcf9f6f3f0edeae7e4e1dedbd8d5d2cfccc9c6c3c0bdbab7b4b1aeaba8a5a29f9c999693908d8a8784817e7b7875726f6c696663605d5a5754514e4b484542"

def hd_public__derive_public__invalid__false():
    seed = bytes.fromhex(SHORT_SEED)

    m = bc.HdPrivate.from_seed(seed, bc.HdPrivate.mainnet)
    m_pub = m.to_public()

    derived = m_pub.derive_public(bc.hd_first_hardened_key)
    assert not derived.is_valid()

def hd_public__encoded__round_trip__expected():
    encoded = "xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8"
    key = bc.HdPublic.from_string(encoded)
    assert key.encoded() == encoded

def hd_public__derive_public__short_seed__expected():
    seed = bytes.fromhex(SHORT_SEED)

    m = bc.HdPrivate.from_seed(seed, bc.HdPrivate.mainnet)
    m0h = m.derive_private(bc.hd_first_hardened_key)
    m0h1 = m0h.derive_private(1)

    m_pub = m.to_public()
    m0h_pub = m.derive_public(bc.hd_first_hardened_key)
    m0h1_pub = m0h_pub.derive_public(1)
    m0h12h_pub = m0h1.derive_public(2 + bc.hd_first_hardened_key)
    m0h12h2_pub = m0h12h_pub.derive_public(2)
    m0h12h2x_pub = m0h12h2_pub.derive_public(1000000000)

    assert m_pub.encoded() == "xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8"
    assert m0h_pub.encoded() == "xpub68Gmy5EdvgibQVfPdqkBBCHxA5htiqg55crXYuXoQRKfDBFA1WEjWgP6LHhwBZeNK1VTsfTFUHCdrfp1bgwQ9xv5ski8PX9rL2dZXvgGDnw"
    assert m0h1_pub.encoded() == "xpub6ASuArnXKPbfEwhqN6e3mwBcDTgzisQN1wXN9BJcM47sSikHjJf3UFHKkNAWbWMiGj7Wf5uMash7SyYq527Hqck2AxYysAA7xmALppuCkwQ"
    assert m0h12h_pub.encoded() == "xpub6D4BDPcP2GT577Vvch3R8wDkScZWzQzMMUm3PWbmWvVJrZwQY4VUNgqFJPMM3No2dFDFGTsxxpG5uJh7n7epu4trkrX7x7DogT5Uv6fcLW5"
    assert m0h12h2_pub.encoded() == "xpub6FHa3pjLCk84BayeJxFW2SP4XRrFd1JYnxeLeU8EqN3vDfZmbqBqaGJAyiLjTAwm6ZLRQUMv1ZACTj37sR62cfN7fe5JnJ7dh8zL4fiyLHV"
    assert m0h12h2x_pub.encoded() == "xpub6H1LXWLaKsWFhvm6RVpEL9P4KfRZSW7abD2ttkWP3SSQvnyA8FSVqNTEcYFgJS2UaFcxupHiYkro49S8yGasTvXEYBVPamhGW6cFJodrTHy"

def hd_public__derive_public__long_seed__expected():
    seed = bytes.fromhex(LONG_SEED)

    m = bc.HdPrivate.from_seed(seed, bc.HdPrivate.mainnet)
    m0 = m.derive_private(0)
    m0xH = m0.derive_private(2147483647 + bc.hd_first_hardened_key)
    m0xH1 = m0xH.derive_private(1)

    m_pub = m.to_public()
    m0_pub = m_pub.derive_public(0)
    m0xH_pub = m0.derive_public(2147483647 + bc.hd_first_hardened_key)
    m0xH1_pub = m0xH_pub.derive_public(1)
    m0xH1yH_pub = m0xH1.derive_public(2147483646 + bc.hd_first_hardened_key)
    m0xH1yH2_pub = m0xH1yH_pub.derive_public(2)

    assert m_pub.encoded() == "xpub661MyMwAqRbcFW31YEwpkMuc5THy2PSt5bDMsktWQcFF8syAmRUapSCGu8ED9W6oDMSgv6Zz8idoc4a6mr8BDzTJY47LJhkJ8UB7WEGuduB"
    assert m0_pub.encoded() == "xpub69H7F5d8KSRgmmdJg2KhpAK8SR3DjMwAdkxj3ZuxV27CprR9LgpeyGmXUbC6wb7ERfvrnKZjXoUmmDznezpbZb7ap6r1D3tgFxHmwMkQTPH"
    assert m0xH_pub.encoded() == "xpub6ASAVgeehLbnwdqV6UKMHVzgqAG8Gr6riv3Fxxpj8ksbH9ebxaEyBLZ85ySDhKiLDBrQSARLq1uNRts8RuJiHjaDMBU4Zn9h8LZNnBC5y4a"
    assert m0xH1_pub.encoded() == "xpub6DF8uhdarytz3FWdA8TvFSvvAh8dP3283MY7p2V4SeE2wyWmG5mg5EwVvmdMVCQcoNJxGoWaU9DCWh89LojfZ537wTfunKau47EL2dhHKon"
    assert m0xH1yH_pub.encoded() == "xpub6ERApfZwUNrhLCkDtcHTcxd75RbzS1ed54G1LkBUHQVHQKqhMkhgbmJbZRkrgZw4koxb5JaHWkY4ALHY2grBGRjaDMzQLcgJvLJuZZvRcEL"
    assert m0xH1yH2_pub.encoded() == "xpub6FnCn6nSzZAw5Tw7cgR9bi15UV96gLZhjDstkXXxvCLsUXBGXPdSnLFbdpq8p9HmGsApME5hQTZ3emM2rnY5agb9rXpVGyy3bdW6EEgAtqt"

hd_public__derive_public__invalid__false()
hd_public__encoded__round_trip__expected()
hd_public__derive_public__short_seed__expected()
hd_public__derive_public__long_seed__expected()

