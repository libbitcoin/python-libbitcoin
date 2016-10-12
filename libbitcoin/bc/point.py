from libbitcoin.bc.config import lib

class Point:

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_point()
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_point(self._obj)

