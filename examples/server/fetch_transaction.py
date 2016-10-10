import sys
import binascii
import zmq.asyncio
import asyncio

loop = zmq.asyncio.ZMQEventLoop()
asyncio.set_event_loop(loop)

import libbitcoin.server
context = libbitcoin.server.Context()

async def main():
    client = context.Client("tcp://gateway.unsystem.net:9091")

    idx = "77cb1e9d44f1b8e8341e6e6848bf34ea6cb7a88bdaad0126ac1254093480f13f"
    idx = bytes.fromhex(idx)

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

