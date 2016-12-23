from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.error import ErrorCode
from libbitcoin.bc.hash import HashDigest
from libbitcoin.bc.input import InputList
from libbitcoin.bc.output import OutputList
from libbitcoin.bc.point import PointIndexes
from libbitcoin.bc.vector import VectorMeta, VectorBase

class Transaction:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_transaction()
        self._obj = obj

    @classmethod
    def from_data(cls, data, wire=True):
        data = DataChunk(data)
        self = cls()
        if wire:
            result = lib.bc_transaction__from_data(self._obj, data._obj)
        else:
            result = lib.bc_transaction__from_data_nowire(self._obj, data._obj)
        if result != 1:
            return None
        return self

    @classmethod
    def from_tuple(cls, version, locktime, inputs, outputs):
        inputs = InputList.from_list(inputs)
        outputs = OutputList.from_list(outputs)
        obj = lib.bc_create_transaction_Parts(version, locktime,
                                              inputs._obj, outputs._obj)
        return cls(obj)

    def __del__(self):
        self._delete_object()

    def _delete_object(self):
        lib.bc_destroy_transaction(self._obj)

    def disable_object_deleter(self):
        self._delete_object = lambda: None

    def copy(self, hash=None):
        if hash is None:
            obj = lib.bc_create_transaction_copy(self._obj)
        else:
            obj = lib.bc_create_transaction_copy_Hash(self._obj, hash._obj)
        return Transaction(obj)

    def __eq__(self, other):
        return lib.bc_transaction__equals(self._obj, other._obj) == 1

    def is_valid(self):
        return lib.bc_transaction__is_valid(self._obj) == 1

    def to_data(self, wire=True):
        if wire:
            obj = lib.bc_transaction__to_data(self._obj)
        else:
            obj = lib.bc_transaction__to_data_nowire(self._obj)
        return DataChunk(obj).data

    def serialized_size(self, wire=True):
        if wire:
            return lib.bc_transaction__serialized_size(self._obj)
        else:
            return lib.bc_transaction__serialized_size_nowire(self._obj)

    def version(self):
        return lib.bc_transaction__version(self._obj)

    def set_version(self, version):
        lib.bc_transaction__set_version(self._obj, version)

    def locktime(self):
        return lib.bc_transaction__locktime(self._obj)

    def set_locktime(self, locktime):
        lib.bc_transaction__set_locktime(self._obj, locktime)

    def inputs(self):
        obj = lib.bc_transaction__inputs(self._obj)
        return list(InputList(obj))

    def set_inputs(self, inputs):
        input_list = InputList.from_list(inputs)
        lib.bc_transaction__set_inputs(self._obj, input_list._obj)

    def outputs(self):
        obj = lib.bc_transaction__outputs(self._obj)
        return list(OutputList(obj))

    def set_outputs(self, outputs):
        output_list = OutputList.from_list(outputs)
        lib.bc_transaction__set_outputs(self._obj, output_list._obj)

    def hash(self, sighash_type=None):
        if sighash_type is None:
            obj = lib.bc_transaction__hash(self._obj)
        else:
            obj = lib.bc_transaction__hash_Sighash(self._obj,
                                                   sighash_type.value)
        return HashDigest(obj)

    def fees(self):
        return lib.bc_transaction__fees(self._obj)

    def double_spends(self, include_unconfirmed):
        obj = lib.bc_transaction__double_spends(self._obj, include_unconfirmed)
        return list(PointIndexes(obj))

    def immature_inputs(self, target_height):
        obj = lib.bc_transaction__immature_inputs(self._obj, target_height)
        return list(PointIndexes(obj))

    def missing_previous_outputs(self):
        obj = lib.bc_transaction__missing_previous_outputs(self._obj)
        return list(PointIndexes(obj))

    def total_input_value(self):
        return lib.bc_transaction__total_input_value(self._obj)

    def total_output_value(self):
        return lib.bc_transaction__total_output_value(self._obj)

    def signature_operations(self, bip16_active):
        return lib.bc_transaction__signature_operations(self._obj,
                                                        bip16_active)

    def is_coinbase(self):
        return lib.bc_transaction__is_coinbase(self._obj) == 1

    def is_null_non_coinbase(self):
        return lib.bc_transaction__is_null_non_coinbase(self._obj) == 1

    def is_oversized_coinbase(self):
        return lib.bc_transaction__is_oversized_coinbase(self._obj) == 1

    def is_immature(self, target_height):
        return lib.bc_transaction__is_immature(self._obj, target_height) == 1

    def is_overspent(self):
        return lib.bc_transaction__is_overspent(self._obj) == 1

    def is_double_spend(self, include_unconfirmed):
        return lib.bc_transaction__is_double_spend(self._obj,
                                                   include_unconfirmed) == 1

    def is_missing_previous_outputs(self):
        return lib.bc_transaction__is_missing_previous_outputs(self._obj) == 1

    def is_final(self, block_height, block_time):
        return lib.bc_transaction__is_final(self._obj,
                                            block_height, block_time) == 1

    def is_locktime_conflict(self):
        return lib.bc_transaction__is_locktime_conflict(self._obj) == 1

    def check(self, transaction_pool=True):
        if transaction_pool:
            obj = lib.bc_transaction__check(self._obj)
        else:
            obj = lib.bc_transaction__check_notransaction_pool(self._obj)
        return ErrorCode(obj)

    def accept(self, transaction_pool=True):
        if transaction_pool:
            obj = lib.bc_transaction__accept(self._obj)
        else:
            obj = lib.bc_transaction__accept_notransaction_pool(self._obj)
        return ErrorCode(obj)

    def connect(self, state):
        obj = lib.bc_transaction__connect(self._obj, state._obj)
        return ErrorCode(obj)

    def connect_input(self, state, input_index):
        obj = lib.bc_transaction__connect(self._obj, state._obj, input_index)
        return ErrorCode(obj)

class TransactionList(VectorBase, metaclass=VectorMeta):
    bc_name = "transaction_list"
    item_type = Transaction

