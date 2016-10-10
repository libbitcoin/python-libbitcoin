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

    idx = "000000000000048b95347e83192f69cf0366076336c639f9b7228e9ba171342e"
    idx = bytes.fromhex(idx)

    ec, height = await client.block_height(idx)
    if ec:
        print("Couldn't fetch block_height:", ec, file=sys.stderr)
        context.stop_all()
        return

    # Should be 210000
    print("Block's height is", height)

    context.stop_all()

if __name__ == '__main__':
    tasks = [
        main(),
    ]
    tasks.extend(context.tasks())
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

