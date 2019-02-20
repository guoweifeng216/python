#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/23 15:45
@filename:rtu_server

"""
from serial import Serial
from collections import defaultdict

from umodbus.server.serial import get_server
from umodbus.server.serial.rtu import RTUServer

s = Serial('com3')
s.timeout = 10

data_store = defaultdict(int)
app = get_server(RTUServer, s)


@app.route(slave_ids=[1], function_codes=[1, 2], addresses=list(range(0, 10)))
def read_data_store(slave_id, function_code, address):
    """" Return value of address. """
    print(data_store[address])
    return data_store[address]


@app.route(slave_ids=[1], function_codes=[5, 15], addresses=list(range(0, 10)))
def write_data_store(slave_id, function_code, address, value):
    """" Set value for address. """
    data_store[address] = value

if __name__ == '__main__':

    try:
        app.serve_forever()
        read_data_store()
    finally:
        app.shutdown()