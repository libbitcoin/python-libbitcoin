import os
from libbitcoin import bc

class Receiver:

    def __init__(self, scan_private, spend_private,
                 version=bc.PaymentAddress.mainnet_p2kh):
        self.scan_private = scan_private
        self.spend_private = spend_private
        self._version = version

    def generate_stealth_address(self):
        # Receiver generates a new scan private.
        scan_public = self.scan_private.to_public()

        # Receiver generates a new spend private.
        spend_public = self.spend_private.to_public()

        stealth_addr = bc.StealthAddress.from_tuple(
            None, scan_public, [spend_public])

        return stealth_addr

    def derive_address(self, ephemeral_public):
        spend_public = self.spend_private.to_public()
        self.receiver_public = bc.uncover_stealth(
            ephemeral_public, self.scan_private, spend_public)

        self.derived_address = bc.PaymentAddress.from_point(
            self.receiver_public, self._version)
        return self.derived_address

    def derive_private(self, ephemeral_public):
        receiver_private = bc.uncover_stealth(
            ephemeral_public, self.scan_private, self.spend_private)
        return receiver_private

class Sender:

    def __init__(self, version=bc.PaymentAddress.mainnet_p2kh):
        self._version = version

    @staticmethod
    def _random_data(size):
        return os.urandom(size)

    @staticmethod
    def _random_ephemeral_secret():
        seed = Sender._random_data(bc.EcSecret.size)
        secret = bc.create_ephemeral_key(seed)
        assert secret is not None
        return secret

    def send_to_stealth_address(self, stealth_addr, ephemeral_private=None):
        # Sender generates a new ephemeral key.
        if ephemeral_private is None:
            ephemeral_private = Sender._random_ephemeral_secret()
        ephemeral_public = ephemeral_private.to_public()

        spend_keys = stealth_addr.spend_keys()
        assert spend_keys

        # Sender derives stealth public, requiring ephemeral private.
        self.sender_public = bc.uncover_stealth(stealth_addr.scan_key(),
                                           ephemeral_private,
                                           spend_keys[0])
        self._send_address = bc.PaymentAddress.from_point(
            self.sender_public, self._version)

        metadata = ephemeral_public.data[1:]
        assert len(metadata) == 32
        meta_script = bc.Script.from_ops([
            bc.Opcode.return_,
            metadata + Sender._random_data(8)
        ])
        return meta_script, self._send_address

# Receiver creates the secret keys.
pocket_main_key = "tprv8ctN3HAF9dCgX9ggdCwiZHa7c3UHuG2Ev4jgYWDhTHDUVWKKsg7znbr3vYtmCzVqcMQsjd9cSKsyKGaDvTAUMkw1UphETe1j8LcT21eWPkH"
main_key = bc.HdPrivate.from_string(pocket_main_key)
# Scan private.
scan_private = main_key.derive_private(
    0 + bc.hd_first_hardened_key).secret()
spend_private = main_key.derive_private(
    1 + bc.hd_first_hardened_key).secret()

receiver = Receiver(scan_private, spend_private, bc.PaymentAddress.testnet_p2kh)
sender = Sender(bc.PaymentAddress.testnet_p2kh)

stealth_addr = receiver.generate_stealth_address()

print("Sending to:", stealth_addr)

assert str(stealth_addr) == "vJmudwspxzmEoz1AP5tTrRMcuop6XjNWa1SnjHFmLeSc9DAkro6J6oYnD7MubLHx9wT3rm7D6xgA8U9Lr9zjzijhVSuUbYdMNYUN27"
# Instead of generating a random ephemeral_private, we are going to
# use this one instead.
ephemeral_private = bc.EcSecret.from_bytes(bytes.fromhex(
    "f91e673103863bbeb0ef1852cd8eade6b73ea55afc9b1873be62bf628eac072a"))

meta_script, send_address = sender.send_to_stealth_address(
    stealth_addr, ephemeral_private)

#########################################
# Send sends BTC to send_address
# Output before is ephemeral_public
# Padded to 40 bytes
#########################################

# Rows:
#   [ephemkey:32] [address:20] [tx_hash:32]

# await client.fetch_stealth()

#########################################
# Receiver scans the blockchain
# And gets a list of keys and addresses for scanning
#########################################

assert bc.is_stealth_script(meta_script)
ephemeral_public = \
    bytes([bc.ephemeral_public_key_sign]) + \
    meta_script.operations()[1].data()[:32]
ephemeral_public = bc.EcCompressed.from_bytes(ephemeral_public)
assert ephemeral_public is not None

print("Derived key:", send_address)
print("Ephemeral key:", ephemeral_public)

assert str(send_address) == "mtKffkQLTw2D6f6mTkrWfi8qxLv4jL1LrK"

# Now the receiver should be able to regenerate the send_address
# using just the ephemeral_public.
if receiver.derive_address(ephemeral_public) == send_address:
    print("Stealth payment detected.")

    # Only reciever can derive stealth private, as it requires both scan
    # and spend private.
    receiver_private = receiver.derive_private(ephemeral_public)

    receiver_public = receiver_private.to_public()
    assert receiver_public == sender.sender_public

    receive_address = bc.PaymentAddress.from_point(
        receiver_public, version=bc.PaymentAddress.testnet_p2kh)

    # Now we've re-derived the same key again.
    # And we also have the private key.
    assert receive_address == send_address
    print("Re-derived address:", receive_address)

    receive_private = receiver.derive_private(ephemeral_public)
    print("Receive private:", receive_private)

    assert receive_private.data.hex() == "fc696c9f7143916f24977210c806101866c7fa13cc06982978d80518c91af2fb"

