from libbitcoin.bc.config import lib
from libbitcoin.bc.output_point import OutputPoint
from libbitcoin.bc.script import Script
from libbitcoin.bc.vector import VectorMeta, VectorBase

class Input:

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

    def copy_previous_output(self):
        obj = lib.bc_input__previous_output(self._obj)
        return OutputPoint(obj)
    def set_previous_output(self, previous_output):
        lib.bc_input__set_previous_output(self._obj, previous_output._obj)

    def copy_script(self):
        obj = lib.bc_input__script(self._obj)
        return Script(obj)
    def set_script(self, script):
        lib.bc_input__set_script(self._obj, script._obj)

    @property
    def sequence(self):
        return lib.bc_input__sequence(self._obj)
    @sequence.setter
    def sequence(self, sequence):
        lib.bc_input__set_sequence(self._obj, sequence)

class InputList(VectorBase, metaclass=VectorMeta):
    bc_name = "input_list"
    item_type = Input
