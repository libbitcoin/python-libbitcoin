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

    address = "13ejSKUxLT9yByyr1bsLNseLbx9H9tNj2d"

    ec, history = await client.history(address)
    if ec:
        print("Couldn't fetch history:", ec, file=sys.stderr)
        context.stop_all()
        return
    for output, spend in history:
        print("OUTPUT point=%s, height=%s, value=%s" %
              (output[0], output[1], output[2]))
        if spend is not None:
            print("-> SPEND point=%s, height=%s" %
                  (spend[0], spend[1]))
        print()

    context.stop_all()

if __name__ == '__main__':
    tasks = [
        main(),
    ]
    tasks.extend(context.tasks())
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

