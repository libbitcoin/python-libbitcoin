from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.hash import HashDigest
from libbitcoin.bc.vector import VectorMeta, VectorBase

class Header:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_header()
        self._obj = obj

    @classmethod
    def from_tuple(cls, values):
        if len(values) == 6:
            values = list(values) + [0]
        obj = lib.bc_create_header_Options(
            values[0],          # version
            values[1]._obj,     # previous block hash
            values[2]._obj,     # merkle
            values[3],          # timestamp
            values[4],          # bits
            values[5],          # nonce
            values[6])          # transaction count
        return cls(obj)

    @classmethod
    def from_data(cls, data, transaction_count=True):
        data = DataChunk(data)
        if transaction_count:
            obj = lib.bc_header__factory_from_data(data._obj)
        else:
            obj = lib.bc_header__factory_from_data_without_transaction_count(
                data._obj)
        return cls(obj)

    def __del__(self):
        lib.bc_destroy_header(self._obj)

    def __eq__(self, other):
        return lib.bc_header__equals(self._obj, other._obj) == 1

    def to_data(self, transaction_count=True):
        if transaction_count:
            obj = lib.bc_header__to_data(self._obj)
        else:
            obj = lib.bc_header__to_data_without_transaction_count(self._obj)
        return DataChunk(obj).data

    def is_valid(self):
        return lib.bc_header__is_valid(self._obj) == 1

    @property
    def version(self):
        return lib.bc_header__version(self._obj)
    @version.setter
    def version(self, version):
        lib.bc_header__set_version(self._obj, version)

    @property
    def previous_block_hash(self):
        obj = lib.bc_header__previous_block_hash(self._obj)
        return HashDigest(obj)
    @previous_block_hash.setter
    def previous_block_hash(self, previous_block_hash):
        lib.bc_header__set_previous_block_hash(self._obj,
                                               previous_block_hash._obj)

    @property
    def merkle(self):
        obj = lib.bc_header__merkle(self._obj)
        return HashDigest(obj)
    @merkle.setter
    def merkle(self, merkle):
        lib.bc_header__set_merkle(self._obj, merkle._obj)

    @property
    def timestamp(self):
        return lib.bc_header__timestamp(self._obj)
    @timestamp.setter
    def timestamp(self, timestamp):
        lib.bc_header__set_timestamp(self._obj, timestamp)

    @property
    def bits(self):
        return lib.bc_header__bits(self._obj)
    @bits.setter
    def bits(self, bits):
        lib.bc_header__set_bits(self._obj, bits)

    @property
    def nonce(self):
        return lib.bc_header__nonce(self._obj)
    @nonce.setter
    def nonce(self, nonce):
        lib.bc_header__set_nonce(self._obj, nonce)

    @property
    def transaction_count(self):
        return lib.bc_header__transaction_count(self._obj)
    @transaction_count.setter
    def transaction_count(self, transaction_count):
        lib.bc_header__set_transaction_count(self._obj, transaction_count)

class HeaderList(VectorBase, metaclass=VectorMeta):
    bc_name = "header_list"
    item_type = Header

