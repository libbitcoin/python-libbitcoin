from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.input import InputList
from libbitcoin.bc.string import String

class Transaction:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_transaction()
        self._obj = obj

    @classmethod
    def from_data(cls, data, satoshi=True):
        data = DataChunk(data)
        if satoshi:
            obj = lib.bc_transaction__factory_from_data(data._obj)
        else:
            obj = lib.bc_transaction__factory_from_data_nosatoshi(data._obj)
        return cls(obj)

    def __del__(self):
        lib.bc_destroy_transaction(self._obj)

    def to_string(self, flags):
        obj = lib.bc_transaction__to_string(self._obj, flags)
        return str(String(obj))

    def __str__(self):
        return self.to_string(0)

    def is_valid(self):
        return lib.bc_transaction__is_valid(self._obj) == 1

    def is_coinbase(self):
        return lib.bc_transaction__is_coinbase(self._obj) == 1

    def is_final(self, block_height, block_time):
        return lib.bc_transaction__is_final(self._obj, block_height,
                                            block_time) == 1

    def is_locktime_conflict(self):
        return lib.bc_transaction__is_locktime_conflict(self._obj) == 1

    @property
    def locktime(self):
        return lib.bc_transaction__locktime(self._obj)
    @locktime.setter
    def locktime(self, locktime):
        lib.bc_transaction__set_locktime(self._obj, locktime)

    def copy_inputs(self):
        obj = lib.bc_transaction__inputs(self._obj)
        return InputList(obj)
    def set_inputs(self, inputs):
        lib.bc_transaction__set_inputs(self._obj, inputs._obj)

