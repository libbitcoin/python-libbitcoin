from libbitcoin import bc

unspent = bc.OutputInfoList()
oi = bc.OutputInfo()
oi.point.base.hash = bc.bitcoin_hash(b"foo")
oi.point.base.index = 110
oi.value = 2
unspent.append(oi)
oi = bc.OutputInfo()
oi.point.base.hash = bc.bitcoin_hash(b"hello")
oi.point.base.index = 4
oi.value = 9
unspent.append(oi)
oi = bc.OutputInfo()
oi.point.base.hash = bc.bitcoin_hash(b"blaaaa")
oi.point.base.index = 99
oi.value = 1
unspent.append(oi)
oi = bc.OutputInfo()
oi.point.base.hash = bc.bitcoin_hash(b"sick")
oi.point.base.index = 8
oi.value = 88
unspent.append(oi)
minimum_value = 10

out = bc.select_outputs(unspent, minimum_value)

for point in out.points:
    print(point)

print(out.change)
