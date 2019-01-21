#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/21 13:42
@filename:rtu_salave

"""
import sys
import modbus_tk
import struct
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time
import serial
import threading
PORT = 'com3'
#PORT = '/dev/ptyp5'
def main():
    """main"""
    global slave_1
    logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")
    #Create the server
    server = modbus_rtu.RtuServer(serial.Serial(PORT))
    try:
        logger.info("running...")
        logger.info("enter 'quit' for closing the server")
        server.start()
        slave_1 = server.add_slave(1)
        slave_1.add_block('0', cst.READ_HOLDING_REGISTERS, 0, 100)
        t = threading.Thread(target=updateData)
        t.setDaemon(True)
        t.start()
        while True:
                cmd = sys.stdin.readline()
                print("input command is {}".format(cmd.split(' ')))
                args = cmd.split(' ')
                print("args is {}".format(args))
                # print("args[0] is {}".format(args[0]))
                # print("args[1] is {}".format(args[1]))
                # print("args[2] is {}".format(args[2]))
                # print("args[3] is {}".format(args[3]))
                if cmd.find('quit') == 0:
                    sys.stdout.write('bye-bye\r\n')
                    break
                elif args[0] == 'add_slave':
                    slave_id = int(args[1])
                    server.add_slave(slave_id)
                    sys.stdout.write('done: slave %d added\r\n' % (slave_id))
                elif args[0] == 'add_block':
                    slave_id = int(args[1])
                    name = args[2]
                    block_type = int(args[3])
                    starting_address = int(args[4])
                    length = int(args[5])
                    slave = server.get_slave(slave_id)
                    slave.add_block(name, block_type, starting_address, length)
                    sys.stdout.write('done: block %s added\r\n' % (name))
                elif args[0] == 'set_values':
                    slave_id = int(args[1])
                    name = args[2]
                    address = int(args[3])
                    values = []
                    for val in args[4:]:
                        values.append(int(val))
                    slave = server.get_slave(slave_id)
                    slave.set_values(name, address, values)
                    values = slave.get_values(name, address, len(values))
                    sys.stdout.write('done: values written: %s\r\n' % (str(values)))
                elif args[0] == 'get_values':
                    slave_id = int(args[1])
                    name = args[2]
                    address = int(args[3])
                    length = int(args[4])
                    slave = server.get_slave(slave_id)
                    values = slave.get_values(name, address, length)
                    sys.stdout.write('done: values read: %s\r\n' % (str(values)))
                else:
                    sys.stdout.write("unknown command %s\r\n" % (args[0]))
    finally:
        server.stop()
#更新值
def updateData():
    global slave_1
    while True:
        slave_1.set_values('0', 3, 88)
        slave_1.set_values('0', 4, 99)
        # print(slave_1.get_values('0',3,2))
        time.sleep(1)
if __name__ == "__main__":
    main()
