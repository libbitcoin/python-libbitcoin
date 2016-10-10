from libbitcoin.bc.config import ffi, lib

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
        self._destroy_object()

    def _destroy_object(self):
        lib.bc_destroy_string(self._obj)

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

class StringListIterator:

    def __init__(self, parent):
        self._parent = parent
        self._index = 0

    def __next__(self):
        if self._index >= len(self._parent):
            raise StopIteration
        result = self._parent[self._index]
        self._index += 1
        return result

class StringList:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_string_list()
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_string_list(self._obj)

    def __getitem__(self, pos):
        obj = lib.bc_string_list__at(self._obj, pos)
        result = String(obj)
        result._destroy_object = lambda: None
        return result

    def __len__(self):
        return lib.bc_string_list__size(self._obj)

    def empty(self):
        return lib.bc_string_list__empty(self._obj)

    def clear(self):
        return lib.bc_string_list__clear(self._obj)

    def __delitem__(self, pos):
        lib.bc_string_list__erase(self._obj, pos)

    def append(self, item):
        # We need to invalidate item's delete function
        item._destroy_object = lambda: None
        lib.bc_string_list__push_back_noconsume(self._obj, item._obj)

    def resize(self, count):
        lib.bc_string_list__resize(self._obj, count)

    def insert(self, pos, item):
        # We need to invalidate item's delete function
        item._destroy_object = lambda: None
        lib.bc_string_list__insert_noconsume(self._obj, pos, item._obj)

    def __iter__(self):
        return StringListIterator(self)

    def __repr__(self):
        return "<bc_string_list [%s]>" % (
            ", ".join([repr(obj) for obj in self]))

