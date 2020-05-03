#!/usr/bin/env python
# -*- coding: utf-8 -*-
# scripts/examples/simple_tcp_server.py
import logging
from socketserver import TCPServer
from collections import defaultdict

from umodbus import conf
from umodbus.server.tcp import RequestHandler, get_server
from umodbus.utils import log_to_stream

# Add stream handler to logger 'uModbus'.
log_to_stream(level=logging.DEBUG)

# A very simple data store which maps addresss against their values.
data_store = defaultdict(int)

# Enable values to be signed (default is False).
conf.SIGNED_VALUES = True

TCPServer.allow_reuse_address = True

address = "0.0.0.0"
port = 502
app = get_server(TCPServer, (address, port), RequestHandler)


@app.route(slave_ids=[1], function_codes=[1, 2], addresses=list(range(7000, 7010)))
def read_data_store(slave_id, function_code, address):
    """" Return value of address. """
    print("read: ", address, data_store[address])
    return data_store[address]


@app.route(slave_ids=[1], function_codes=[6, 15], addresses=list(range(7000, 7010)))
def write_data_store(slave_id, function_code, address, value):
    """" Set value for address. """
    data_store[address] = value
    print("write: ", address, data_store[address])

if __name__ == '__main__':
    try:
        print("starting modbus server on port: ", port)
        app.serve_forever()
    finally:
        print("shutting down modbus server on port: ", port)
        app.shutdown()
        app.server_close()
