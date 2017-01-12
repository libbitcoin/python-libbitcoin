import sys
import binascii
import zmq.asyncio
import asyncio

loop = zmq.asyncio.ZMQEventLoop()
asyncio.set_event_loop(loop)

import libbitcoin.server
context = libbitcoin.server.Context()

async def main():
    #client = context.Client("tcp://gateway.unsystem.net:9091")
    #address = "13ejSKUxLT9yByyr1bsLNseLbx9H9tNj2d"

    client = context.Client("tcp://163.172.84.141:9091")
    address = "mqWKk5FUVAoUYZmKLtaEqhm8G7vQ345mWn"

    ec, history = await client.history(address)
    if ec:
        print("Couldn't fetch history:", ec, file=sys.stderr)
        context.stop()
        return
    for output, spend in history:
        print("OUTPUT point=%s, height=%s, value=%s" %
              (output[0], output[1], output[2]))
        if spend is not None:
            print("-> SPEND point=%s, height=%s" %
                  (spend[0], spend[1]))
        print()
    # Calculate the balance of a Bitcoin address from its history.
    balance = sum(output[2] for output, spend in history if spend is None)
    print("Address balance:", balance)

    context.stop()

if __name__ == '__main__':
    loop.run_until_complete(main())
    loop.close()

