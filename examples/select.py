from libbitcoin import bc

unspent = [
    ((bc.bitcoin_hash(b"foo"), 110), 2),
    ((bc.bitcoin_hash(b"hello"), 4), 9),
    ((bc.bitcoin_hash(b"blaaaa"), 99), 1),
    ((bc.bitcoin_hash(b"sick"), 8), 88)
]

minimum_value = 10

out = bc.select_outputs(unspent, minimum_value)

for point in out.points:
    print(point)

print(out.change)
