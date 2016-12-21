import zmq

#url = "tcp://gateway.unsystem.net:9094"
url = "tcp://163.172.84.141:9094"

context = zmq.Context()

socket = context.socket(zmq.SUB)
socket.connect(url)
socket.setsockopt(zmq.SUBSCRIBE, b"")

while True:
    response = socket.recv_multipart()
    print(response)

