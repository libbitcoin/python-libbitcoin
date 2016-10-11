from libbitcoin.bc.config import lib
from libbitcoin.bc.input import InputList
from libbitcoin.bc.string import String

class Transaction:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_transaction()
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_transaction(self._obj)

    def to_string(self, flags):
        obj = lib.bc_transaction__to_string(self._obj, flags)
        return str(String(obj))

    def __str__(self):
        return self.to_string(0)

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

