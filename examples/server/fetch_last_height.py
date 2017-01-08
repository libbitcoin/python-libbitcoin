import sys
import zmq.asyncio
import asyncio

loop = zmq.asyncio.ZMQEventLoop()
asyncio.set_event_loop(loop)

import libbitcoin.server
context = libbitcoin.server.Context()

tor_enabled = True

async def main():
    if tor_enabled:
        url = "tcp://iqqy3y6bdjpdij3i.onion:9091"
    else:
        url = "tcp://gateway.unsystem.net:9091"
        # Testnet URL
        url = "tcp://163.172.84.141:9091"

    client_settings = libbitcoin.server.ClientSettings()
    client_settings.query_expire_time = 10.0
    if tor_enabled:
        client_settings.socks5 = "127.0.0.1:9150"

    print("Connecting:", url)

    client = context.Client(url, settings=client_settings)

    ec, height = await client.last_height()
    if ec:
        print("Couldn't fetch last_height:", ec, file=sys.stderr)
        context.stop()
        return
    print("Last height:", height)

    ec, total_connections = await client.total_connections()
    if ec:
        print("Couldn't fetch total_connections:", ec, file=sys.stderr)
        context.stop()
        return
    print("Total server connections:", total_connections)

    context.stop()

if __name__ == '__main__':
    tasks = [
        main(),
    ]
    tasks.extend(context.tasks())
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

