import sys
import binascii
import zmq.asyncio
import asyncio

loop = zmq.asyncio.ZMQEventLoop()
asyncio.set_event_loop(loop)

import libbitcoin.server
context = libbitcoin.server.Context()

async def main():
    client = context.Client("tcp://163.172.84.141:8081")
    #client = context.Client("tcp://gateway.unsystem.net:9091")

    idx = "083207bea408c5eaf8a2c625ea6a7ecf3fdabe9642a574d01408d61e096cbbfb"
    idx = bytes.fromhex(idx)[::-1]

    ec, tx_data = await client.transaction(idx)
    if ec:
        print("Couldn't fetch transaction:", ec, file=sys.stderr)
        context.stop_all()
        return
    # Should be 257 bytes.
    print("tx size is %s bytes" % len(tx_data))

    ec, height, index = await client.transaction_index(idx)
    if ec:
        print("Couldn't fetch transaction_index:", ec, file=sys.stderr)
        context.stop_all()
        return
    # 210000 4
    print(height, index)

    context.stop_all()

if __name__ == '__main__':
    tasks = [
        main(),
    ]
    tasks.extend(context.tasks())
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

