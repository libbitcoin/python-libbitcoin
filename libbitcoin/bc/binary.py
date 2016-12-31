from libbitcoin.bc.config import lib
from libbitcoin.bc.constants import max_size_t
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.string import String

class Binary:

    bits_per_block = lib.bc_binary__bits_per_block()

    @staticmethod
    def blocks_size(bit_size):
        return lib.bc_binary__blocks_size(bit_size)

    @staticmethod
    def is_base2(text):
        return lib.bc_is_base2(text) == 1

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_binary()
        self._obj = obj

    def from_string(cls, bit_string):
        obj = lib.bc_create_binary_String(bit_string)
        return cls(obj)

    def from_data(cls, size, blocks):
        blocks = DataChunk(blocks)
        obj = lib.bc_create_binary_Blocks(size, blocks._obj)
        return cls(obj)

    def __del__(self):
        lib.bc_destroy_binary(self._obj)

    def resize(self, size):
        return lib.bc_binary__resize(self._obj, size)

    def __getitem__(self, index):
        return lib.bc_binary__at(self._obj, index) == 1

    def blocks(self):
        obj = lib.bc_binary__blocks(self._obj)
        return DataChunk(obj).data

    def encoded(self):
        obj = lib.bc_binary__encoded(self._obj)
        return str(String(obj))

    # size in bits
    def __len__(self):
        return lib.bc_binary__size(self._obj)

    def append(self, post):
        lib.bc_binary__append(self._obj, post._obj)

    def prepend(self, prior):
        lib.bc_binary__prepend(self._obj, post._obj)

    def shift_left(self, distance):
        lib.bc_binary__shift_left(self._obj, distance)

    def shift_right(self, distance):
        lib.bc_binary__shift_right(self._obj, distance)

    def substring(self, first, length=max_size_t):
        obj = lib.bc_binary__substring_Length(self._obj, first, length)
        return str(String(obj))

    def is_prefix_of(self, field):
        # Either data, uint32_t or binary
        # TODO: not sure how to implement the uint8_t* args
        assert False

    def __eq__(self, other):
        return lib.bc_binary__equals(self._obj, other._obj) == 1

