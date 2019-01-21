#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/12 10:42
@filename:read_register

"""
# !/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python
 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr
 This is distributed under GNU LGPL license, see license.txt
"""

import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

# PORT = 1
# PORT = "/dev/ttyUSB0"
PORT = "COM3"

def main():
    """main"""
    logger = modbus_tk.utils.create_logger("console")

    try:
        # Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info("connected")
        # master.close()
        # print(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10))
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 4,0,1,12,34,4a))
        # print(type((master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10)[2])))
        # print(master.execute(1, cst.WRITE_SINGLE_REGISTER, 3, 10))

        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 16))
        # logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 0,1,0x07d0))

        # 读保持寄存器
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 16))
        # 读输入寄存器
        # logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 0, 16))
        # 读线圈寄存器
        #logger.info(master.execute(1, cst.READ_COILS, 0, 16))
        # 读离散输入寄存器
        #logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 16))
        # 单个读写寄存器操作
        # 写寄存器地址为0的保持寄存器
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 12, output_value=0x1))
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 12, 4))
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 2, output_value=0x41f0))
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 2, 4))
        # 写寄存器地址为0的线圈寄存器，写入内容为0（位操作）
        #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 0, output_value=0))
        #logger.info(master.execute(1, cst.READ_COILS, 0, 1))
        # 多个寄存器读写操作
        # 写寄存器起始地址为0的保持寄存器，操作寄存器个数为4
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 11, output_value=[0x1, 0x1, 0x1, 0x1]))
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 11, 4))
        # 写寄存器起始地址为0的线圈寄存器
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0, 0, 0, 0]))
        #logger.info(master.execute(1, cst.READ_COILS, 0, 4))

        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 4))
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1))
        # logger.info(master.execute(1, cst.READ_COILS, 0, 10))
        # send some queries
        # logger.info(master.execute(1, cst.READ_COILS, 0, 10))
        # logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 8))
        # logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 100, 3))
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
        # logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
        # logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 100, output_value=54))
        # logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
        # logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))

    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())


if __name__ == "__main__":
    main()
