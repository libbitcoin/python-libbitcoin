#!/usr/bin/python3
import tornado.ioloop
import tornado.web
from zmq.eventloop.ioloop import IOLoop

import libbitcoin

# Debug stuff
import logging
logging.basicConfig(level=logging.DEBUG)

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, client):
        self._client = client

    def get(self):
        loop.add_callback(foo)

    async def get(self):
        ec, height = await self._client.last_height()
        if ec:
            self.write("Error reading block height: %s" % ec)
            return
        self.write("Last block height is %s" % height)

def make_app(context):
    client = context.Client("tcp://gateway.unsystem.net:9091")
    return tornado.web.Application([
        (r"/", MainHandler, dict(client=client)),
    ])

if __name__ == "__main__":
    context = libbitcoin.TornadoContext()
    app = make_app(context)
    app.listen(8888)
    loop = IOLoop.current()
    context.start(loop)
    loop.start()

