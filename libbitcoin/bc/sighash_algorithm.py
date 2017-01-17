from enum import Enum
from libbitcoin.bc.config import lib

class SighashAlgorithm(Enum):

    all = lib.bc_sighash_algorithm__all
    none = lib.bc_sighash_algorithm__none
    single = lib.bc_sighash_algorithm__single
    anyone_can_pay = lib.bc_sighash_algorithm__anyone_can_pay
    all_anyone_can_pay = lib.bc_sighash_algorithm__all_anyone_can_pay
    none_anyone_can_pay = lib.bc_sighash_algorithm__none_anyone_can_pay
    single_anyone_can_pay = lib.bc_sighash_algorithm__single_anyone_can_pay

