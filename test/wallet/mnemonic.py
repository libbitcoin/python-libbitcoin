from libbitcoin import bc
import wallet.mnemonic_data as mnemonic_data

def mnemonic__decode_mnemonic__no_passphrase():
    for item in mnemonic_data.mnemonic_no_passphrase:
        entropy, mnemonic, passphrase, seed, language = item
        words = mnemonic.split(",")
        assert bc.validate_mnemonic(words, bc.Dictionary.en)
        mnemonic_seed = bc.decode_mnemonic(words)
        assert mnemonic_seed.encode_base16() == seed

def mnemonic__create_mnemonic__trezor():
    for item in mnemonic_data.mnemonic_trezor_vectors:
        entropy, mnemonic, passphrase, seed, language = item
        entropy = bytes.fromhex(entropy)
        mnemonic_words = bc.create_mnemonic(entropy,
                                            bc.Dictionary.get(language))
        assert mnemonic_words
        assert ",".join(mnemonic_words) == mnemonic
        assert bc.validate_mnemonic(mnemonic_words)

def mnemonic__create_mnemonic__bx():
    for item in mnemonic_data.mnemonic_bx_new_vectors:
        entropy, mnemonic, passphrase, seed, language = item
        entropy = bytes.fromhex(entropy)
        mnemonic_words = bc.create_mnemonic(entropy,
                                            bc.Dictionary.get(language))
        assert mnemonic_words
        assert ",".join(mnemonic_words) == mnemonic
        assert bc.validate_mnemonic(mnemonic_words)

def mnemonic__validate_mnemonic__invalid():
    for mnemonic in mnemonic_data.invalid_mnemonic_tests:
        words = mnemonic.split(",")
        assert not bc.validate_mnemonic(words)

def mnemonic__create_mnemonic__tiny():
    entropy = bytes([0xa9] * 4)
    mnemonic = bc.create_mnemonic(entropy)
    assert len(mnemonic) == 3
    assert bc.validate_mnemonic(mnemonic)

def mnemonic__create_mnemonic__giant():
    entropy = bytes([0xa9] * 1024)
    mnemonic = bc.create_mnemonic(entropy)
    assert len(mnemonic) == 768
    assert bc.validate_mnemonic(mnemonic)

def mnemonic__dictionary__en_es__no_intersection():
    english = bc.Dictionary.en
    spanish = bc.Dictionary.es
    intersection = 0
    for es in spanish:
        for en in english:
            if es == en:
                intersection += 1
    assert intersection == 0

def mnemonic__dictionary__zh_Hans_Hant__intersection():
    simplified = bc.Dictionary.zh_Hans
    traditional = bc.Dictionary.zh_Hant
    intersection = 0
    for hant in traditional:
        for hans in simplified:
            if hant == hans:
                intersection += 1
    assert intersection == 1275

mnemonic__decode_mnemonic__no_passphrase()
mnemonic__create_mnemonic__trezor()
mnemonic__create_mnemonic__bx()
mnemonic__validate_mnemonic__invalid()
mnemonic__create_mnemonic__tiny()
mnemonic__create_mnemonic__giant()
# Slow tests. Skipped.
#mnemonic__dictionary__en_es__no_intersection()
#mnemonic__dictionary__zh_Hans_Hant__intersection()

