from libbitcoin.bc.binary import Binary
from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.elliptic_curve import EcCompressed, PointList
from libbitcoin.bc.payment_address import PaymentAddress
from libbitcoin.bc.string import String

mainnet_p2kh = lib.bc_stealth_address__mainnet_p2kh()

class StealthAddress:

    mainnet_p2kh = lib.bc_stealth_address__mainnet_p2kh()
    reuse_key_flag = lib.bc_stealth_address__reuse_key_flag()
    max_filter_bits = lib.bc_stealth_address__max_filter_bits()

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_stealth_address()
        self._obj = obj

    @classmethod
    def from_data(cls, decoded):
        decoded = DataChunk(decoded)
        obj = lib.bc_create_stealth_address_Data(decoded._obj)
        return cls(obj)

    @classmethod
    def from_string(cls, encoded):
        obj = lib.bc_create_stealth_address_String(encoded)
        return cls(obj)

    @classmethod
    def from_tuple(cls, filter_, scan_key, spend_keys,
                   signatures=0, version=mainnet_p2kh):
        if filter_ is None:
            filter_ = Binary()
        elif isinstance(filter, str):
            filter_ = Binary.from_string(filter_)
        spend_keys = PointList.from_list(spend_keys)
        obj = lib.bc_create_stealth_address_Options(
            filter_._obj, scan_key._obj, spend_keys._obj, signatures, version)
        return cls(obj)

    def __del__(self):
        lib.bc_destroy_stealth_address(self._obj)

    def _eq__(self, other):
        return lib.bc_stealth_address__equals(self._obj, other._obj)

    def is_valid(self):
        return lib.bc_stealth_address__is_valid() == 1

    def encoded(self):
        obj = lib.bc_stealth_address__encoded(self._obj)
        return str(String(obj))

    def __str__(self):
        return self.encoded()

    def version(self):
        return lib.bc_stealth_address__version(self._obj)

    def scan_key(self):
        obj = lib.bc_stealth_address__scan_key(self._obj)
        return EcCompressed(obj)

    def spend_keys(self):
        obj = lib.bc_stealth_address__spend_keys(self._obj)
        return list(PointList(obj))

    def signatures(self):
        return lib.bc_stealth_address__signatures(self._obj)

    def filter(self):
        obj = lib.bc_stealth_address__filter(self._obj)

    def to_chunk(self):
        obj = lib.bc_stealth_address__to_chunk(self._obj)
        return DataChunk(obj).data

