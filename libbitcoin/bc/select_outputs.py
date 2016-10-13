from libbitcoin.bc.config import lib
from libbitcoin.bc.output_point import PointsInfo

def select_outputs(unspent, minimum_value):
    out = PointsInfo()
    lib.bc_select_outputs_select(out._obj, unspent._obj, minimum_value)
    return out

