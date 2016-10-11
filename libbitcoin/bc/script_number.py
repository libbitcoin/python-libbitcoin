from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.data import DataChunk

class ScriptNumber:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_script_number_default()
        elif isinstance(obj, int):
            obj = lib.bc_create_script_number(obj)
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_script_number(self._obj)

    @property
    def data(self):
        obj = lib.bc_script_number__data(self._obj)
        return DataChunk(obj).data

