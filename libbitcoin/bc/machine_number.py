from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.data import DataChunk

class MachineNumber:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_machine_number()
        elif isinstance(obj, int):
            obj = lib.bc_create_machine_number_Value(obj)
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_machine_number(self._obj)

    def data(self):
        obj = lib.bc_machine_number__data(self._obj)
        return DataChunk(obj).data

