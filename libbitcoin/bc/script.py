from enum import Enum
from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.error import ErrorCode
from libbitcoin.bc.operation import OperationStack
from libbitcoin.bc.string import String

class ScriptParseMode(Enum):
    strict = lib.bc_script_parse_mode__strict
    raw_data = lib.bc_script_parse_mode__raw_data
    raw_data_fallback = lib.bc_script_parse_mode__raw_data_fallback

class Script:

    @staticmethod
    def verify(tx, input_index, flags):
        obj = lib.bc_script__verify(tx._obj, input_index, flags.value)
        return ErrorCode(obj)

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_script()
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_script(self._obj)

    def is_raw_data(self):
        return lib.bc_script__is_raw_data(self._obj) == 1

    def from_data(self, data, prefix, parse_mode):
        data = DataChunk(data)
        return lib.bc_script__from_data(self._obj, data._obj,
                                        prefix, parse_mode.value) == 1

    def to_data(self, prefix):
        obj = lib.bc_script__to_data(self._obj, prefix)
        return DataChunk(obj).data

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

    def copy_operations(self):
        obj = lib.bc_script__operations(self._obj)
        return OperationStack(obj)
    def set_operations(self, ops):
        lib.bc_script__set_operations(self._obj, ops._obj)

