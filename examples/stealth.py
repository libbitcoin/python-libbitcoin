import os
from libbitcoin import bc

pocket_main_key = "tprv8ctN3HAF9dCgX9ggdCwiZHa7c3UHuG2Ev4jgYWDhTHDUVWKKsg7znbr3vYtmCzVqcMQsjd9cSKsyKGaDvTAUMkw1UphETe1j8LcT21eWPkH"

main_key = bc.HdPrivate.from_string(pocket_main_key)

# Receiver generates a new scan private.
scan_private = main_key.derive_private(0 + bc.hd_first_hardened_key).secret()
scan_public = scan_private.to_public()

# Receiver generates a new spend private.
spend_private = main_key.derive_private(1 + bc.hd_first_hardened_key).secret()
spend_public = spend_private.to_public()

stealth_addr = bc.StealthAddress.from_tuple(
    None, scan_public, [spend_public])
print("Sending to:", stealth_addr)

# Sender generates a new ephemeral key.
ephemeral_data = os.urandom(bc.EcSecret.size)
ephemeral_private = bc.EcSecret.from_bytes(ephemeral_data)
ephemeral_public = ephemeral_private.to_public()

# Sender derives stealth public, requiring ephemeral private.
sender_public = bc.uncover_stealth(scan_public, ephemeral_private,
                                   spend_public)
send_addr = bc.PaymentAddress.from_point(sender_public,
                                         version=bc.PaymentAddress.testnet_p2kh)

print("Derived address:", send_addr)
print("Ephem key:", ephemeral_public)
print()

#########################################
# Send sends BTC to send_addr
# Output before is ephemeral_public
# Padded to 40 bytes
#########################################

#########################################
# Receiver scans the blockchain
# And gets a list of keys and addrs for scanning
#########################################

# Rows:
#   [ephemkey:32] [address:20] [tx_hash:32]

# Now the receiver should be able to regenerate the send_addr
# using just the ephemeral_public.

receiver_public = bc.uncover_stealth(ephemeral_public, scan_private,
                                     spend_public)

# Only reciever can derive stealth private, as it requires both scan
# and spend private.
receiver_private = bc.uncover_stealth(ephemeral_public, scan_private,
                                     spend_private)
receiver_public2 = receiver_private.to_public()

assert receiver_public == receiver_public2

receive_addr = bc.PaymentAddress.from_point(receiver_public,
                                            version=bc.PaymentAddress.testnet_p2kh)

# Now we've re-derived the same key again.
# And we also have the private key.
assert receive_addr == send_addr
print("Re-derived address:", receive_addr)

