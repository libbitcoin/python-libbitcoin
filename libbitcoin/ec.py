import hashlib
import os
import ecdsa
from ecdsa.util import string_to_number, number_to_string
from libbitcoin.bitcoin_utils import hash_160_to_bc_address, hash_160

# secp256k1, http://www.oid-info.com/get/1.3.132.0.10
_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
_b = 0x0000000000000000000000000000000000000000000000000000000000000007
_a = 0x0000000000000000000000000000000000000000000000000000000000000000
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
_Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(_p, _a, _b)
generator_secp256k1 = ecdsa.ellipticcurve.Point(
    curve_secp256k1, _Gx, _Gy, _r)
oid_secp256k1 = (1, 3, 132, 0, 10)
SECP256k1 = ecdsa.curves.Curve(
    "SECP256k1",
    curve_secp256k1,
    generator_secp256k1,
    oid_secp256k1
)
ec_order = _r

def GetPubKey(pubkey, compressed=False):
    # public keys are 65 bytes long (520 bits)
    # 0x04 + 32-byte X-coordinate + 32-byte Y-coordinate
    # 0x00 = point at infinity, 0x02 and 0x03 = compressed, 0x04 = uncompressed
    # compressed keys:
    # <sign> <x> where <sign> is 0x02 if y is even and 0x03 if y is odd
    if compressed:
        if pubkey.point.y() & 1:
            key = '03' + '%064x' % pubkey.point.x()
        else:
            key = '02' + '%064x' % pubkey.point.x()
    else:
        key = '04' + \
              '%064x' % pubkey.point.x() + \
              '%064x' % pubkey.point.y()
    return bytes.fromhex(key)

class EC_KEY(object):
    def __init__(self, secret):
        self.pubkey = ecdsa.ecdsa.Public_key(
            generator_secp256k1,
            generator_secp256k1 * secret
        )
        self.privkey = ecdsa.ecdsa.Private_key(self.pubkey, secret)
        self.secret = secret

    def sign_message(self, message, compressed, address):
        private_key = ecdsa.SigningKey.from_secret_exponent(
            self.secret, curve=SECP256k1
        )
        public_key = private_key.get_verifying_key()
        signature = private_key.sign_digest(
            Hash(msg_magic(message)), sigencode=ecdsa.util.sigencode_string
        )
        assert public_key.verify_digest(
            signature,
            Hash(msg_magic(message)),
            sigdecode=ecdsa.util.sigdecode_string
        )
        for i in range(4):
            sig = base64.b64encode(
                chr(27 + i + (4 if compressed else 0)) + signature
            )
            try:
                self.verify_message(address, sig, message)
                return sig
            except:
                continue
        else:
            raise BaseException("error: cannot sign message")

    @classmethod
    def verify_message(self, address, signature, message):
        """See http://www.secg.org/download/aid-780/sec1-v2.pdf
           for the math"""
        import msqr
        curve = curve_secp256k1
        G = generator_secp256k1
        order = G.order()
        # extract r,s from signature
        sig = base64.b64decode(signature)
        if len(sig) != 65:
            raise BaseException("Wrong encoding")
        r, s = ecdsa.util.sigdecode_string(sig[1:], order)
        nV = ord(sig[0])
        if nV < 27 or nV >= 35:
            raise BaseException("Bad encoding")
        if nV >= 31:
            compressed = True
            nV -= 4
        else:
            compressed = False

        recid = nV - 27
        # 1.1
        x = r + (recid/2) * order
        # 1.3
        alpha = (x * x * x + curve.a() * x + curve.b()) % curve.p()
        beta = msqr.modular_sqrt(alpha, curve.p())
        y = beta if (beta - recid) % 2 == 0 else curve.p() - beta
        # 1.4 the constructor checks that nR is at infinity
        R = ecdsa.ellipticcurve.Point(curve, x, y, order)
        # 1.5 compute e from message:
        h = Hash(msg_magic(message))
        e = string_to_number(h)
        minus_e = -e % order
        # 1.6 compute Q = r^-1 (sR - eG)
        inv_r = ecdsa.numbertheory.inverse_mod(r, order)
        Q = inv_r * (s * R + minus_e * G)
        public_key = ecdsa.VerifyingKey.from_public_point(Q, curve=SECP256k1)
        # check that Q is the public key
        public_key.verify_digest(
            sig[1:], h, sigdecode=ecdsa.util.sigdecode_string
        )
        # check that we get the original signing address
        addr = public_key_to_bc_address(encode_point(public_key, compressed))
        if address != addr:
            raise BaseException("Bad signature")

class EllipticCurveKey:

    def __init__(self):
        self._secret = None
        self._private_key = None
        self._public_key = None

    def new_key_pair(self):
        secret = os.urandom(32)
        self.set_secret(secret)

    def set_secret(self, secret):
        self._secret = secret
        secret = string_to_number(secret)
        pkey = EC_KEY(secret)

        #sec = "L5KhaMvPYRW1ZoFmRjUtxxPypQ94m6BcDrPhqArhggdaTbbAFJEF"
        #pkey = obelisk.regenerate_key(sec)

        secexp = pkey.secret
        self._private_key = ecdsa.SigningKey.from_secret_exponent(
            secexp, curve=SECP256k1)
        self._public_key = self._private_key.get_verifying_key()

    def sign(self, digest):
        if self._private_key is None:
            return None
        return self._private_key.sign_digest_deterministic(
            digest, hashfunc=hashlib.sha256,
            sigencode=ecdsa.util.sigencode_der)

    def verify(self, digest, signature):
        if self._public_key is None:
            return None
        return self._public_key.verify_digest(
            signature, digest, sigdecode=ecdsa.util.sigdecode_der)

    @property
    def secret(self):
        return self._secret

    @property
    def public_key(self):
        return GetPubKey(self._public_key.pubkey, True)

    @property
    def key_id(self):
        return hash_160(self.public_key)

    @property
    def address(self):
        return hash_160_to_bc_address(0, self.key_id)

if __name__ == "__main__":
    import binascii
    ec = EllipticCurveKey()
    ec.new_key_pair()
    sig = ec.sign(b"123")
    assert ec.verify(b"123", sig)

