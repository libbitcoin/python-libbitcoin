from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.output_point import OutputPoint
from libbitcoin.bc.script import Script
from libbitcoin.bc.string import String
from libbitcoin.bc.vector import VectorMeta, VectorBase

class Input:

    @classmethod
    def from_data(cls, data):
        data = DataChunk(data)
        obj = lib.bc_input__factory_from_data(data._obj)
        return cls(obj)

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_input()
        self._obj = obj

    def __del__(self):
        self._delete_object()

    def _delete_object(self):
        lib.bc_destroy_input(self._obj)

    def disable_object_deleter(self):
        self._delete_object = lambda: None

    def __eq__(self, other):
        return lib.bc_input__equals(self._obj, other._obj) == 1

    def to_data(self):
        obj = lib.bc_input__to_data(self._obj)
        return DataChunk(obj).data

    def is_valid(self):
        return lib.bc_input__is_valid(self._obj) == 1

    def serialized_size(self):
        return lib.bc_input__serialized_size(self._obj)

    def previous_output(self):
        obj = lib.bc_input__previous_output(self._obj)
        return OutputPoint(obj)

    def set_previous_output(self, previous_output):
        lib.bc_input__set_previous_output(self._obj, previous_output._obj)

    def script(self):
        obj = lib.bc_input__script(self._obj)
        return Script(obj)

    def set_script(self, script):
        lib.bc_input__set_script(self._obj, script._obj)

    def sequence(self):
        return lib.bc_input__sequence(self._obj)

    def set_sequence(self, sequence):
        lib.bc_input__set_sequence(self._obj, sequence)

    def __repr__(self):
        return "<bc_input>"

class InputList(VectorBase, metaclass=VectorMeta):
    bc_name = "input_list"
    item_type = Input
