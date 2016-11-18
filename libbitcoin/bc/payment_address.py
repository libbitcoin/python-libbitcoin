from libbitcoin.bc.config import ffi, lib
from libbitcoin.bc.ec_private import EcPrivate
from libbitcoin.bc.elliptic_curve import EcSecret
from libbitcoin.bc.hash import ShortHash
from libbitcoin.bc.string import String

class PaymentAddress:

    mainnet_p2kh = lib.bc_payment_address__mainnet_p2kh()
    mainnet_p2sh = lib.bc_payment_address__mainnet_p2sh()

    def __init__(self, obj=None):
        if isinstance(obj, str):
            obj = PaymentAddress._string_init_obj(obj)
        if obj is None:
            obj = lib.bc_create_payment_address()
        self._obj = obj

    @staticmethod
    def _string_init_obj(address):
        address = bytes(address, "ascii")
        return lib.bc_create_payment_address_String(address)

    @classmethod
    def extract(cls, script, p2kh_version=None, p2sh_version=None):
        if p2kh_version is None and p2sh_version is None:
            obj = lib.bc_payment_address__extract(script._obj)
        elif p2kh_version is not None and p2sh_version is None:
            obj = lib.bc_payment_address__extract_Version(
                script._obj, p2kh_version)
        else:
            obj = lib.bc_payment_address__extract_Options(
                script._obj, p2kh_version, p2sh_version)
        return cls(obj)

    @classmethod
    def from_string(cls, address):
        return cls(PaymentAddress._string_init_obj(address))

    @classmethod
    def from_hash(cls, hash_, version=None):
        if version is None:
            obj = lib.bc_create_payment_address_Hash(hash_._obj)
        else:
            obj = lib.bc_create_payment_address_Hash_Version(
                hash_._obj, version)
        return cls(obj)

    @classmethod
    def from_secret(cls, secret):
        if isinstance(secret, EcSecret):
            secret = EcPrivate.from_secret(secret)
        obj = lib.bc_create_payment_address_Secret(secret._obj)
        return cls(obj)

    @classmethod
    def from_point(cls, point, version=None):
        if version is None:
            obj = lib.bc_create_payment_address_Point(point._obj)
        else:
            obj = lib.bc_create_payment_address_Point_Version(
                point._obj, version)
        return cls(obj)

    @classmethod
    def from_script(cls, script, version=None):
        if version is None:
            obj = lib.bc_create_payment_address_Script(script._obj)
        else:
            obj = lib.bc_create_payment_address_Script_Version(
                script._obj, version)
        return cls(obj)

    def __del__(self):
        lib.bc_destroy_payment_address(self._obj)

    def clone(self):
        obj = lib.bc_create_payment_address_copy(self._obj)
        return PaymentAddress(obj)

    def is_valid(self):
        return lib.bc_payment_address__is_valid(self._obj) == 1

    def encoded(self):
        obj = lib.bc_payment_address__encoded(self._obj)
        return str(String(obj))

    @property
    def version(self):
        return lib.bc_payment_address__version(self._obj)

    @property
    def hash(self):
        obj = lib.bc_payment_address__hash(self._obj)
        return ShortHash(obj)

    def __eq__(self, other):
        return lib.bc_payment_address__equals(self._obj, other._obj) == 1

    def __str__(self):
        return self.encoded()

    def __repr__(self):
        return "<bc_payment_address '%s'>" % self.encoded()

