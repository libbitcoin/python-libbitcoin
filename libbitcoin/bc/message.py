from libbitcoin.bc.config import lib
from libbitcoin.bc.data import DataChunk
from libbitcoin.bc.ec_private import EcPrivate
from libbitcoin.bc.byte_array import ByteArrayBase, ByteArrayMeta
from libbitcoin.bc.payment_address import PaymentAddress

def hash_message(message):
    message = DataChunk(message)
    return lib.hash_message(message._obj)

def sign_message(message, secret):
    signature = MessageSignature()
    message = DataChunk(message)
    assert isinstance(secret, EcPrivate)
    if lib.bc_sign_message(signature._obj, message._obj, secret._obj) != 1:
        return None
    return signature.data

def verify_message(message, address, signature):
    message = DataChunk(message)
    if isinstance(address, str):
        address = PaymentAddress(address)
    assert isinstance(address, PaymentAddress)
    signature = MessageSignature.from_bytes(signature)
    return lib.bc_verify_message(message._obj, address._obj, signature._obj) \
        == 1

#def recovery_id_to_magic(recovery_id, compressed):
#    pass
#
#def magic_to_recovery_id(magic):
#    pass

class MessageSignature(ByteArrayBase, metaclass=ByteArrayMeta):
    bc_name = "message_signature"

