from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.vector import VectorMeta, VectorBase

class String:

    def __init__(self, s=None):
        if type(s) == str:
            s = s.encode()
        if s is None:
            self._obj = lib.bc_create_string_default()
        elif type(s) == bytes:
            self._obj = lib.bc_create_string_Length(s, len(s))
        else:
            self._obj = s

    def __del__(self):
        self._delete_object()

    def _delete_object(self):
        lib.bc_destroy_string(self._obj)

    def disable_object_deleter(self):
        self._delete_object = lambda: None

    @property
    def data(self):
        return ffi.string(lib.bc_string__data(self._obj), len(self))

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return "<bc_string '%s'>" % str(self)

    def empty(self):
        return lib.bc_string__empty(self._obj)

    def __eq__(self, s):
        if type(s) == str:
            s = s.encode()

        if type(s) == bytes:
            return lib.bc_string__equals_cstr(self._obj, s) == 1
        else:
            return lib.bc_string__equals(self._obj, s._obj) == 1

    def __len__(self):
        return lib.bc_string__length(self._obj)

class StringList(VectorBase, metaclass=VectorMeta):
    bc_name = "string_list"
    item_type = String

