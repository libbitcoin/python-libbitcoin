from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.hash import HashDigest
from libbitcoin.bc.string import String
from libbitcoin.bc.vector import VectorMeta, VectorBase, \
                                 IntVectorMeta, IntVectorBase

class Point:

    null_index = lib.bc_point__null_index()

    @classmethod
    def from_data(cls, data):
        data = DataChunk(data)
        obj = lib.bc_point__factory_from_data(data._obj)
        return cls(obj)

    @staticmethod
    def satoshi_fixed_size():
        return lib.bc_point__satoshi_fixed_size()

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_point()
        self._obj = obj

    def __del__(self):
        self._delete_object()

    def _delete_object(self):
        lib.bc_destroy_point(self._obj)

    def disable_object_deleter(self):
        self._delete_object = lambda: None

    def __eq__(self, other):
        return lib.bc_point__equals(self._obj, other._obj) == 1

    def checksum(self):
        return lib.bc_point__checksum(self._obj)

    def is_null(self):
        return lib.bc_point__is_null(self._obj)

    def to_data(self):
        obj = lib.bc_point__to_data(self._obj)
        return DataChunk(obj)

    def to_string(self):
        obj = lib.bc_point__to_string(self._obj)
        return str(String(obj))

    def __str__(self):
        return self.to_string()

    def is_valid(self):
        return lib.bc_point__is_valid(self._obj) == 1

    def reset(self):
        lib.bc_point__reset(self._obj)

    def serialized_size(self):
        return lib.bc_point__serialized_size(self._obj)

    def hash(self):
        obj = lib.bc_point__hash(self._obj)
        return HashDigest(obj)

    def set_hash(self, hash_):
        lib.bc_point__set_hash(self._obj, hash_._obj)

    def index(self):
        return lib.bc_point__index(self._obj)

    def set_index(self, index):
        lib.bc_point__set_index(self._obj, index)

    def __repr__(self):
        return "<bc_point %s:%s>" % (str(self.hash), self.index)

class ChainPointList(VectorBase, metaclass=VectorMeta):
    bc_name = "chain_point_list"
    item_type = Point

class PointIndexes(IntVectorBase, metaclass=IntVectorMeta):
    bc_name = "point_indexes"

