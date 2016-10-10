from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.string import String

class Script:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_script()
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_script(self._obj)

    def from_data(self, data, prefix, parse_mode):
        data = DataChunk(data)
        return lib.bc_script__from_data(self._obj, data._obj,
                                        prefix, parse_mode) == 1

    def to_data(self, prefix):
        obj = lib.bc_script__to_data(self._obj, prefix)
        return DataChunk(obj).value

    def from_string(self, human_readable):
        if type(human_readable) == str:
            human_readable = bytes(human_readable, "ascii")
        return lib.bc_script__from_string(self._obj, human_readable) == 1

    def to_string(self, flags):
        obj = lib.bc_script__to_string(self._obj, flags)
        return str(String(obj))

    def is_valid(self):
        return lib.bc_script__is_valid(self._obj) == 1

    def __str__(self):
        return self.to_string(0)

    def __repr__(self):
        return "<bc_script '%s'>" % str(self)

