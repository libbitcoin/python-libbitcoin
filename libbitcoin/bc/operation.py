from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.opcode import Opcode
from libbitcoin.bc.vector import VectorMeta, VectorBase

class Operation:

    def __init__(self, obj=None, data=b""):
        if isinstance(obj, Opcode):
            self._init_from_tuple(obj, data)
            return
        if obj is None:
            obj = lib.bc_create_operation()
        self._obj = obj

    def _init_from_tuple(self, code, data):
        self._obj = lib.bc_create_operation()
        self.code = code
        self.data = data

    @classmethod
    def from_tuple(cls, code, data):
        return cls(code, data)

    def __del__(self):
        self._delete_object()

    def _delete_object(self):
        lib.bc_destroy_operation(self._obj)

    def disable_object_deleter(self):
        self._delete_object = lambda: None

    def is_valid(self):
        lib.bc_operation__is_valid(self._obj)

    @property
    def code(self):
        return Opcode(lib.bc_operation__code(self._obj))
    @code.setter
    def code(self, code):
        lib.bc_operation__set_code(self._obj, code.value)

    @property
    def data(self):
        obj = lib.bc_operation__data(self._obj)
        return DataChunk(obj).data
    @data.setter
    def data(self, data):
        data = DataChunk(data)
        lib.bc_operation__set_data(self._obj, data._obj)

    def __repr__(self):
        return "<bc_operation (%s, %s)>" % (self.code.name, self.data.hex())

class OperationStack(VectorBase, metaclass=VectorMeta):
    bc_name = "operation_stack"
    item_type = Operation

