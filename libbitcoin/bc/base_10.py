from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.string import String

btc_decimal_places = lib.bc_btc_decimal_places()
mbtc_decimal_places = lib.bc_mbtc_decimal_places()
ubtc_decimal_places = lib.bc_ubtc_decimal_places()

def decode_base10(amount, decimal_places=None, strict=True):
    """Validates and parses an amount string according to the BIP 21 grammar.
    @param decmial_places the location of the decimal point.
    The default is 0, which treats the input as a normal integer.
    @param strict true to treat fractional results as an error,
    or false to round them upwards.
    @return None for failure."""
    if isinstance(amount, str):
        amount = bytes(amount, "ascii")
    out = ffi.new("uint64_t *")
    if decimal_places is None:
        success = lib.bc_decode_base10(out, amount)
    elif strict:
        success = lib.bc_decode_base10_Places(out, amount, decimal_places)
    else:
        success = lib.bc_decode_base10_Places_nostrict(out, amount,
                                                       decimal_places)
    if success == 0:
        return None
    return out[0]

def encode_base10(amount, decimal_places=None):
    """Writes a Bitcoin amount to a string, following the BIP 21 grammar.
    Avoids the rounding issues often seen with floating-point methods.
    @param decmial_places the location of the decimal point.
    The default is 0, which treats the input as a normal integer."""
    if decimal_places is None:
        result = lib.bc_encode_base10(amount)
    else:
        result = lib.bc_encode_base10_Places(amount, decimal_places)
    return str(String(result))

