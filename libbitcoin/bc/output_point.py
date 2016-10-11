from libbitcoin.bc.config import lib
from libbitcoin.bc.output import Output

class OutputPoint:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_output_point()
        self._obj = obj

    @classmethod
    def from_tuple(cls, hash_, index):
        obj = lib.bc_create_output_point_Tuple(hash_.obj, index)
        return cls(obj)

    def __del__(self):
        lib.bc_destroy_output_point(self._obj)

    def copy_cache(self):
        obj = lib.bc_output_point__cache(self._obj)
        return Output(obj)
    def set_cache(self, cache):
        lib.bc_output_point__set_cache(self._obj, cache._obj)

