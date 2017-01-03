from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.script import Script
from libbitcoin.bc.string_ import String
from libbitcoin.bc.vector import VectorMeta, VectorBase

class Output:

    not_found = lib.bc_output__not_found()

    @classmethod
    def from_data(cls, data):
        data = DataChunk(data)
        obj = lib.bc_output__factory_from_data(data._obj)
        return cls(obj)

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_output()
        self._obj = obj

    def __del__(self):
        self._delete_object()

    def _delete_object(self):
        lib.bc_destroy_output(self._obj)

    def disable_object_deleter(self):
        self._delete_object = lambda: None

    def __eq__(self, other):
        return lib.bc_output__equals(self._obj, other._obj) == 1

    def to_data(self):
        obj = lib.bc_output__to_data(self._obj)
        return DataChunk(obj).data

    def to_string(self, flags):
        obj = lib.bc_output__to_string(self._obj, flags)
        return str(String(obj))

    def __str__(self):
        return self.to_string(0)

    def is_valid(self):
        return lib.bc_output__is_valid(self._obj) == 1

    def reset(self):
        lib.bc_output__reset(self._obj)

    def serialized_size(self):
        return lib.bc_output__serialized_size(self._obj)

    def signature_operations(self):
        return lib.bc_output__signature_operations(self._obj)

    def value(self):
        return lib.bc_output__value(self._obj)

    def set_value(self, value):
        lib.bc_output__set_value(self._obj, value)

    def script(self):
        obj = lib.bc_output__script(self._obj)
        return Script(obj)

    def set_script(self, script):
        lib.bc_output__set_script(self._obj, script._obj)

class OutputList(VectorBase, metaclass=VectorMeta):
    bc_name = "output_list"
    item_type = Output

