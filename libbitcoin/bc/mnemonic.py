from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.hash import LongHash
from libbitcoin.bc.string_ import String, StringList

def mnemonic_to_string_list(mnemonic):
    result = StringList()
    for word in mnemonic:
        result.append(String(word))
    return result

def mnemonic_word_multiple():
    """A valid mnemonic word count is evenly divisible by this number."""
    return bc_mnemonic_word_multiple()

def mnemonic_seed_multiple():
    """A valid seed byte count is evenly divisible by this number."""
    return bc_mnemonic_seed_multiple()

def create_mnemonic(entropy, lexicon=None):
    """Create a new mnenomic (list of words) from provided entropy
    and a dictionary selection. The mnemonic can later be converted to
    a seed for use in wallet creation. Entropy byte count must be
    evenly divisible by 4."""
    entropy = DataChunk(entropy)
    if lexicon is None:
        obj = lib.bc_create_mnemonic(entropy._obj)
    else:
        obj = lib.bc_create_mnemonic_Dict(entropy._obj, lexicon._obj)
    return [str(word) for word in StringList(obj)]

def validate_mnemonic(mnemonic, lexicon=None):
    """Checks a mnemonic against a dictionary to determine if the
    words are spelled correctly and the checksum matches.
    The words must have been created using mnemonic encoding.
    
    If lexicon is None then check that a mnemonic is valid in at
    least one of the provided languages."""
    mnemonic = mnemonic_to_string_list(mnemonic)
    if lexicon is None:
        return lib.bc_validate_mnemonic_all_languages(mnemonic._obj) == 1
    else:
        return lib.bc_validate_mnemonic(mnemonic._obj, lexicon._obj) == 1

def decode_mnemonic(mnemonic):
    """Convert a mnemonic with no passphrase to a wallet-generation seed."""
    mnemonic = mnemonic_to_string_list(mnemonic)
    obj = lib.bc_decode_mnemonic(mnemonic._obj)
    return LongHash(obj)

