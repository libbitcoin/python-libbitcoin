from libbitcoin.bc.config import ffi, lib

class VectorMeta(type):

    def __new__(cls, clsname, bases, attrs):
        bc_name = attrs["bc_name"]
        def method(method_name):
            return getattr(lib, method_name % bc_name)
        attrs["bc_create_vector"] = method("bc_create_%s")
        attrs["bc_destroy_vector"] = method("bc_destroy_%s")
        attrs["bc_vector__at"] = method("bc_%s__at")
        attrs["bc_vector__size"] = method("bc_%s__size")
        attrs["bc_vector__empty"] = method("bc_%s__empty")
        attrs["bc_vector__clear"] = method("bc_%s__clear")
        attrs["bc_vector__erase"] = method("bc_%s__erase")
        attrs["bc_vector__push_back_noconsume"] = \
            method("bc_%s__push_back_noconsume")
        attrs["bc_vector__resize"] = method("bc_%s__resize")
        attrs["bc_vector__insert_noconsume"] = \
            method("bc_%s__insert_noconsume")
        return super().__new__(cls, clsname, bases, attrs)

class VectorIterator:

    def __init__(self, parent):
        self._parent = parent
        self._index = 0

    def __next__(self):
        if self._index >= len(self._parent):
            raise StopIteration
        result = self._parent[self._index]
        self._index += 1
        return result

class VectorBase:

    def __init__(self, obj=None):
        if obj is None:
            obj = self.bc_create_vector()
        self._obj = obj

    def __del__(self):
        self.bc_destroy_vector(self._obj)

    def __getitem__(self, pos):
        obj = self.bc_vector__at(self._obj, pos)
        result = self.item_type(obj)
        result.disable_object_deleter()
        return result

    def __len__(self):
        return self.bc_vector__size(self._obj)

    def empty(self):
        return self.bc_vector__empty(self._obj)

    def clear(self):
        return self.bc_vector__clear(self._obj)

    def __delitem__(self, pos):
        self.bc_vector__erase(self._obj, pos)

    def append(self, item):
        # We need to invalidate item's delete function
        item.disable_object_deleter()
        self.bc_vector__push_back_noconsume(self._obj, item._obj)

    def resize(self, count):
        self.bc_vector__resize(self._obj, count)

    def insert(self, pos, item):
        # We need to invalidate item's delete function
        item.disable_object_deleter()
        self.bc_vector__insert_noconsume(self._obj, pos, item._obj)

    def __iter__(self):
        return VectorIterator(self)

    def __repr__(self):
        return "<bc_%s [%s]>" % (self.bc_name,
            ", ".join([repr(obj) for obj in self]))

