import sys
import binascii
import zmq.asyncio
import asyncio

loop = zmq.asyncio.ZMQEventLoop()
asyncio.set_event_loop(loop)

import libbitcoin
context = libbitcoin.Context()

async def main():
    client = context.Client("tcp://gateway.unsystem.net:9091")

    idx = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    idx = bytes.fromhex(idx)

    ec, header = await client.block_header(idx)
    if ec:
        print("Couldn't fetch block_header:", ec, file=sys.stderr)
        context.stop_all()
        return
    print("Header:", binascii.hexlify(header))

    context.stop_all()

if __name__ == '__main__':
    tasks = [
        main(),
    ]
    tasks.extend(context.tasks())
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

