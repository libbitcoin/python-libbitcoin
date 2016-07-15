import zmq.asyncio
import asyncio

loop = zmq.asyncio.ZMQEventLoop()
asyncio.set_event_loop(loop)

import libbitcoin
context = libbitcoin.Context()

async def main():
    client_settings = libbitcoin.ClientSettings()
    client_settings.query_expire_time = None

    client = context.Client("tcp://gateway.unsystem.net:9091",
                            settings=client_settings)

    ec, height = await client.last_height()
    assert ec is None
    print("Last height:", height)

    ec, total_connections = await client.total_connections()
    assert ec is None
    print("Total server connections:", total_connections)

    context.stop_all()

if __name__ == '__main__':
    tasks = [
        main(),
    ]
    tasks.extend(context.tasks())
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

