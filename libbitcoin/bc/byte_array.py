from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.string_ import String

class ByteArrayMeta(type):

    def __new__(cls, clsname, bases, attrs):
        bc_name = attrs["bc_name"]
        def method(method_name):
            return getattr(lib, method_name % bc_name)
        attrs["bc_create_object"] = method("bc_create_%s")
        attrs["bc_create_object_Data"] = method("bc_create_%s_Data")
        attrs["bc_create_object_Base16"] = method("bc_create_%s_Base16")
        attrs["bc_destroy_object"] = method("bc_destroy_%s")
        attrs["bc_object__data"] = method("bc_%s__data")
        attrs["bc_object__encode_base16"] = method("bc_%s__encode_base16")
        def bc_object_size():
            return getattr(lib, "bc_%s_size" % bc_name)()
        attrs["size"] = bc_object_size()
        return super().__new__(cls, clsname, bases, attrs)

class ByteArrayBase:

    def __init__(self, obj=None):
        if obj is None:
            obj = self.bc_create_object()
        self._obj = obj

    @classmethod
    def from_bytes(cls, data):
        obj = cls.bc_create_object_Data(data)
        return cls(obj)

    @classmethod
    def from_string(cls, data, reversed_literal=False):
        if type(data) == str:
            data = bytes.fromhex(data)
        if reversed_literal:
            data = data[::-1]
        return cls.from_bytes(data)

    def __del__(self):
        self._delete_object()

    def _delete_object(self):
        self.bc_destroy_object(self._obj)

    def disable_object_deleter(self):
        self._delete_object = lambda: None

    def __len__(self):
        return self.size

    @property
    def data(self):
        return ffi.buffer(self.bc_object__data(self._obj), len(self))[:]

    def encode_base16(self):
        obj = self.bc_object__encode_base16(self._obj)
        return str(String(obj))

    def __str__(self):
        return self.encode_base16()

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return "<bc_%s '%s'>" % (self.bc_name, self.encode_base16())

