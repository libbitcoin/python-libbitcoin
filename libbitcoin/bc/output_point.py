from libbitcoin.bc.config import lib
from libbitcoin.bc.output import Output
from libbitcoin.bc.point import Point, ChainPointList
from libbitcoin.bc.vector import VectorMeta, VectorBase

class Validation:

    not_specified = lib.bc_output_point_validation__not_specified()

    def __init__(self, obj):
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_output_point_validation(self._obj)

    @property
    def spent(self):
        return lib.bc_output_point_validation__spent(self._obj)
    @spent.setter
    def spent(self, spent):
        lib.bc_output_point_validation__set_spent(self._obj, spent)

    @property
    def confirmed(self):
        return lib.bc_output_point_validation__confirmed(self._obj)
    @confirmed.setter
    def confirmed(self, confirmed):
        lib.bc_output_point_validation__set_confirmed(self._obj, confirmed)

    @property
    def height(self):
        return lib.bc_output_point_validation__height(self._obj)
    @height.setter
    def height(self, height):
        lib.bc_output_point_validation__set_height(self._obj, height)

    @property
    def cache(self):
        obj = lib.bc_output_point_validation__cache(self._obj)
        return Output(obj)

class OutputPoint:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_output_point()
        self._obj = obj

    @classmethod
    def from_tuple(cls, hash_, index):
        if isinstance(hash_, bytes):
            hash_ = bc.HashDigest.from_bytes(hash_)
        obj = lib.bc_create_output_point_Tuple(hash_._obj, index)
        return cls(obj)

    @classmethod
    def from_point(cls, point):
        return cls.from_tuple(point.hash(), point.index())

    def __del__(self):
        lib.bc_destroy_output_point(self._obj)

    @property
    def base(self):
        base_obj = lib.bc_output_point__point_Base(self._obj)
        return Point(base_obj)

    def hash(self):
        return self.base.hash()

    def index(self):
        return self.base.index()

    def __eq__(self, other):
        return lib.bc_output_point__equals(self._obj, other._obj) == 1

    def is_mature(self, target_height):
        return lib.bc_output_point__is_mature(self._obj, target_height)

    @property
    def validation(self):
        obj = lib.bc_output_point__validation(self._obj)
        return Validation(obj)

    def __repr__(self):
        return "<bc_output_point>"

class PointsInfo:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_points_info()
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_points_info(self._obj)

    @property
    def points(self):
        obj = lib.bc_points_info__points(self._obj)
        return list(ChainPointList(obj))
    @points.setter
    def points(self, points):
        lib.bc_points_info__set_points(self._obj, points._obj)

    @property
    def change(self):
        return lib.bc_points_info__change(self._obj)
    @change.setter
    def change(self, change):
        lib.bc_points_info__set_change(self._obj, change)

    def __repr__(self):
        return "<bc_points_info>"

class OutputInfo:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_output_info()
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_output_info(self._obj)

    @property
    def point(self):
        obj = lib.bc_output_info__point(self._obj)
        return OutputPoint(obj)
    @point.setter
    def point(self, point):
        lib.bc_output_info__set_point(self._obj, point._obj)

    @property
    def value(self):
        return lib.bc_output_info__value(self._obj)
    @value.setter
    def value(self, value):
        lib.bc_output_info__set_value(self._obj, value)

    def __repr__(self):
        return "<bc_output_info>"

class OutputInfoList(VectorBase, metaclass=VectorMeta):
    bc_name = "output_info_list"
    item_type = OutputInfo

