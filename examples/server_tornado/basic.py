import asyncio
import signal
from libbitcoin.server_fake_async import TornadoContext, Client

async def hello(client):
    await asyncio.sleep(2.0)
    print("Querying...")
    print(await client.last_height())

def main():
    context = TornadoContext()

    url = "tcp://gateway.unsystem.net:9091"
    client = Client(context, url)

    def signal_handler(signum, frame):
        print("Stopping darkwallet-daemon...")
        context.stop()

    context.spawn(hello, client)

    signal.signal(signal.SIGINT, signal_handler)
    context.start()

main()

