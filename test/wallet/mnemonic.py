from libbitcoin import bc
import wallet.mnemonic_data as mnemonic_data

def mnemonic__decode_mnemonic__no_passphrase():
    for item in mnemonic_data.mnemonic_no_passphrase:
        entropy, mnemonic, passphrase, seed, language = item
        words = mnemonic.split(",")

mnemonic__decode_mnemonic__no_passphrase()

