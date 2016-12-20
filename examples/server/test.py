import random
import struct
import sys
import zmq

def create_random_id():
    MAX_UINT32 = 4294967295
    return random.randint(0, MAX_UINT32)

url = "tcp://gateway.unsystem.net:9091"
#url = "tcp://5.135.30.59:9091"

c = zmq.Context()

s = c.socket(zmq.DEALER)
s.connect(url)

command = b"blockchain.fetch_last_height"
ident = create_random_id()
data = b""

request = [
    command,
    struct.pack('<I', ident),
    data
]
s.send_multipart(request)

response = s.recv_multipart()

command, response_ident, data = response
assert struct.unpack('<I', response_ident)[0] == ident
error = struct.unpack('<I', data[:4])[0]
if error:
    print("Error returning height", file=sys.stderr)
    sys.exit(-1)

height = struct.unpack('<I', data[4:])[0]
print("Height:", height)

