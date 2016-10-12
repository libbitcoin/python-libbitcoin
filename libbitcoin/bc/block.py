from libbitcoin.bc.config import lib
from libbitcoin.bc.transaction import TransactionList

class Block:

    @classmethod
    def genesis_mainnet(cls):
        obj = lib.bc_block__genesis_mainnet()
        return cls(obj)

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_block()
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_block(self._obj)

    def copy_transactions(self):
        obj = lib.bc_block__transactions(self._obj)
        return TransactionList(obj)
    def set_transactions(self, transactions):
        lib.bc_block__set_transactions(self._obj, transactions._obj)

