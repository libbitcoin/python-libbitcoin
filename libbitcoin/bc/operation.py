from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.opcode_ import Opcode
from libbitcoin.bc.vector import VectorMeta, VectorBase

class Operation:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_operation()
        self._obj = obj

    @classmethod
    def from_data(cls, uncoded, minimal=True):
        data = DataChunk(uncoded)
        if minimal:
            obj = lib.bc_create_operation_Data(data._obj)
        else:
            obj = lib.bc_create_operation_Data_nominimal(data._obj)
        return cls(obj)

    @classmethod
    def from_opcode(cls, code):
        obj = lib.bc_create_operation_Opcode(code.value)
        return cls(obj)

    def __del__(self):
        self._delete_object()

    def _delete_object(self):
        lib.bc_destroy_operation(self._obj)

    def disable_object_deleter(self):
        self._delete_object = lambda: None

    def is_valid(self):
        lib.bc_operation__is_valid(self._obj)

    def to_data(self):
        obj = lib.bc_operation__to_data(self._obj)
        return DataChunk(obj).data

    def code(self):
        return Opcode(lib.bc_operation__code(self._obj))

    def data(self):
        obj = lib.bc_operation__data(self._obj)
        return DataChunk(obj).data

    def __repr__(self):
        return "<bc_operation (%s, %s)>" % (self.code.name, self.data.hex())

class OperationList(VectorBase, metaclass=VectorMeta):
    bc_name = "operation_list"
    item_type = Operation

