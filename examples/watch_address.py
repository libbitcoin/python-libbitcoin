import binascii
import zmq.asyncio
import asyncio

loop = zmq.asyncio.ZMQEventLoop()
asyncio.set_event_loop(loop)

import libbitcoin
context = libbitcoin.Context()

def hash_str(hash):
    return str(binascii.hexlify(hash), "ascii")

async def main():
    client = context.Client("tcp://obelisk.airbitz.co:9091")

    address = "15s5nojkHKxJz3GvpKD1S6DR9nKUxSzNko"
    #prefix = libbitcoin.Binary.from_address(address)
    prefix = libbitcoin.Binary.from_string("11")
    ec, subscription = await client.subscribe_address(prefix)
    assert ec is None
    print("Watching address: %s..." % address)
    print("prefix=%s" % prefix)

    # Stop after 1 minute.
    loop.call_later(60, lambda: loop.create_task(subscription.stop()))

    with subscription:
        while subscription.is_running():
            update = await subscription.updates()
            print("Received update:")
            if update.confirmed:
                print("Block #%s %s" % (update.height,
                                        hash_str(update.block_hash)))
            tx_hash = libbitcoin.bitcoin_utils.bitcoin_hash(update.tx_data)
            print("Transaction:", hash_str(tx_hash))

    context.stop_all()

if __name__ == '__main__':
    tasks = [
        main(),
    ]
    tasks.extend(context.tasks())
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

