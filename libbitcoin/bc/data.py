import binascii
from libbitcoin.bc.config import ffi, lib

class DataChunk:

    def __init__(self, data=None):
        if data is None:
            self._obj = lib.bc_create_data_chunk()
        elif type(data) == bytes:
            self._obj = lib.bc_create_data_chunk_Array(data, len(data))
        else:
            self._obj = data

    def __del__(self):
        lib.bc_destroy_data_chunk(self._obj)

    def clone(self):
        obj = lib.bc_create_data_chunk_copy(self._obj)
        return DataChunk(obj)
        
    def __len__(self):
        return lib.bc_data_chunk__size(self._obj)

    def resize(self, count):
        lib.bc_data_chunk__resize(self, count)

    @property
    def data(self):
        raw_data = lib.bc_data_chunk__data(self._obj)
        if raw_data == ffi.NULL:
            return b""
        return ffi.buffer(raw_data, len(self))[:]

    def extend(self, other):
        if type(other) != DataChunk:
            other = DataChunk(other)
        lib.bc_data_chunk__extend_data(self._obj, other._obj)

    def __eq__(self, other):
        if type(other) != DataChunk:
            other = DataChunk(other)
        return lib.bc_data_chunk__equals(self._obj, other._obj) == 1

    def __str__(self):
        return self.data.hex()

    def __repr__(self):
        return "<bc_data_chunk '%s'>" % self.data.hex()

