import sys
import zmq.asyncio
import asyncio

loop = zmq.asyncio.ZMQEventLoop()
asyncio.set_event_loop(loop)

import libbitcoin
context = libbitcoin.Context()

async def main():
    #client = context.Client("tcp://gateway.unsystem.net:9091")
    client = context.Client("tcp://obelisk.airbitz.co:9091")

    prefix = libbitcoin.Binary.from_string("11")
    ec, rows = await client.stealth(prefix, 419135)
    if ec:
        print("Couldn't fetch stealth:", ec, file=sys.stderr)
        context.stop_all()
        return

    print("Fetched %s rows." % len(rows))

    context.stop_all()

if __name__ == '__main__':
    tasks = [
        main(),
    ]
    tasks.extend(context.tasks())
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

