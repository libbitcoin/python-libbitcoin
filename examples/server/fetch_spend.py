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

    outpoint = libbitcoin.server.OutPoint()
    outpoint.hash = bytes.fromhex(
        "0530375a5bf4ea9a82494fcb5ef4a61076c2af807982076fa810851f4bc31c09")
    outpoint.index = 0

    ec, spend = await client.spend(outpoint)
    if ec:
        print("Couldn't fetch spend:", ec, file=sys.stderr)
        context.stop_all()
        return

    check_spend = libbitcoin.server.InPoint()
    check_spend.hash = bytes.fromhex(
        "e03a9a4b5c557f6ee3400a29ff1475d1df73e9cddb48c2391abdc391d8c1504a")
    check_spend.index = 0
    if spend != check_spend:
        print("Incorrect spend value supplied by server.")
        context.stop_all()
        return

    print(spend)

    context.stop_all()

if __name__ == '__main__':
    tasks = [
        main(),
    ]
    tasks.extend(context.tasks())
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

