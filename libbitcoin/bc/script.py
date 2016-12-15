from enum import Enum
from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.error import ErrorCode
from libbitcoin.bc.hash import HashDigest
from libbitcoin.bc.operation import OperationList
from libbitcoin.bc.string import String

class SignatureHashAlgorithm(Enum):
    all = lib.bc_sighash_algorithm__all
    none = lib.bc_sighash_algorithm__none
    single = lib.bc_sighash_algorithm__single
    anyone_can_pay = lib.bc_sighash_algorithm__anyone_can_pay
    all_anyone_can_pay = lib.bc_sighash_algorithm__all_anyone_can_pay
    none_anyone_can_pay = lib.bc_sighash_algorithm__none_anyone_can_pay
    single_anyone_can_pay = lib.bc_sighash_algorithm__single_anyone_can_pay
    mask = lib.bc_sighash_algorithm__mask

class Script:

    @staticmethod
    def generate_signature_hash(parent_tx, input_index,
                                script_code, sighash_type):
        obj = lib.bc_script__generate_signature_hash(
            parent_tx._obj, input_index, script_code._obj, sighash_type.value)
        return HashDigest(obj)

    @staticmethod
    def create_endorsement(out, secret, prevout_script, new_tx,
                           input_index, sighash_type):
        return lib.bc_script__create_endorsement(
            out._obj, secret._obj, prevout_script._obj, new_tx._obj,
            input_index, sighash_type.value) == 1

    @staticmethod
    def check_signature(signature, sighash_type, public_key,
                        script_code, parent_tx, input_index):
        public_key = DataChunk(public_key)
        return lib.bc_script__check_signature(
            signature._obj, sighash_type.value, public_key._obj,
            script_code._obj, parent_tx._obj, input_index) == 1
    
    @staticmethod
    def verify(tx, input_index, flags):
        obj = lib.bc_script__verify(tx._obj, input_index, flags.value)
        return ErrorCode(obj)

    def __init__(self, obj=None):
        if obj is None:
            obj = lib.bc_create_script()
        self._obj = obj

    def __del__(self):
        lib.bc_destroy_script(self._obj)

    def is_raw_data(self):
        return lib.bc_script__is_raw_data(self._obj) == 1

    def from_data(self, data, prefix, parse_mode):
        data = DataChunk(data)
        return lib.bc_script__from_data(self._obj, data._obj,
                                        prefix, parse_mode.value) == 1

    def to_data(self, prefix):
        obj = lib.bc_script__to_data(self._obj, prefix)
        return DataChunk(obj).data

    def from_string(self, human_readable):
        if type(human_readable) == str:
            human_readable = bytes(human_readable, "ascii")
        return lib.bc_script__from_string(self._obj, human_readable) == 1

    def to_string(self, flags):
        obj = lib.bc_script__to_string(self._obj, flags)
        return str(String(obj))

    def is_valid(self):
        return lib.bc_script__is_valid(self._obj) == 1

    def __str__(self):
        return self.to_string(0)

    def __repr__(self):
        return "<bc_script '%s'>" % str(self)

    @property
    def operations(self):
        obj = lib.bc_script__operations(self._obj)
        return OperationList(obj)
    @operations.setter
    def operations(self, ops):
        lib.bc_script__set_operations(self._obj, ops._obj)

