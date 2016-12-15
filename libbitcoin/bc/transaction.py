from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.hash import HashDigest
from libbitcoin.bc.input import InputList
from libbitcoin.bc.output import OutputList
from libbitcoin.bc.string import String
from libbitcoin.bc.vector import VectorMeta, VectorBase

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
        self._delete_object()

    def _delete_object(self):
        lib.bc_destroy_transaction(self._obj)

    def disable_object_deleter(self):
        self._delete_object = lambda: None

    def to_data(self, satoshi=True):
        if satoshi:
            obj = lib.bc_transaction__to_data(self._obj)
        else:
            obj = lib.bc_transaction__to_data_nosatoshi(self._obj)
        return DataChunk(obj).data

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

    def serialized_size(self):
        return lib.bc_transaction__serialized_size(self._obj)

    def total_output_value(self):
        return lib.bc_transaction__total_output_value(self._obj)

    def hash(self, sighash_type=None):
        if sighash_type is None:
            obj = lib.bc_transaction__hash(self._obj)
        else:
            obj = lib.bc_transaction__hash_Sighash(self._obj,
                                                   sighash_type.value)
        return HashDigest(obj)

    @property
    def locktime(self):
        return lib.bc_transaction__locktime(self._obj)
    @locktime.setter
    def locktime(self, locktime):
        lib.bc_transaction__set_locktime(self._obj, locktime)

    def inputs(self):
        obj = lib.bc_transaction__inputs(self._obj)
        return list(InputList(obj))
    def set_inputs(self, inputs):
        input_list = InputList()
        [input_list.append(input) for input in inputs]
        lib.bc_transaction__set_inputs(self._obj, input_list._obj)

    def outputs(self):
        obj = lib.bc_transaction__outputs(self._obj)
        return list(OutputList(obj))
    def set_outputs(self, outputs):
        output_list = OutputList()
        [output_list.append(output) for output in outputs]
        lib.bc_transaction__set_outputs(self._obj, output_list._obj)

class TransactionList(VectorBase, metaclass=VectorMeta):
    bc_name = "transaction_list"
    item_type = Transaction

