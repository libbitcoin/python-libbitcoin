from libbitcoin.bc.config import lib
from libbitcoin.bc.output_point import OutputInfoList, OutputInfo, PointsInfo

def select_outputs(unspent, minimum_value):
    bc_unspent = OutputInfoList()
    for row in unspent:
        hash, index = row[0]
        value = row[1]
        info = OutputInfo()
        info.point.base.set_hash(hash)
        info.point.base.set_index(index)
        info.value = value
        bc_unspent.append(info)
    out = PointsInfo()
    lib.bc_select_outputs__select(out._obj, bc_unspent._obj, minimum_value)
    return out

