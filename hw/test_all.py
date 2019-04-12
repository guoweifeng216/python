#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/3/7 14:35
@filename:test_all

"""
import os
import sys
from optparse import OptionParser
import subprocess as sub
# sys.path.append(os.path.join(os.path.dirname(__file__)))
from resource import auto_full_temp_mix
from resource import auto_full_temp_read
from resource import auto_full_temp_write
from resource import auto_MS_aver_BW_mix
from resource import auto_MS_aver_BW_seq_read
from resource import auto_MS_aver_BW_seq_write

class RunScriptt(object):
    def __init__(self,host, user, passwd, serial_port ='COM4',baudrate = 9600 ):
        self.cmd_path = r"C:\Users\cnex\Desktop\IOmeter-free\Iometer_with_log"
        self.temp_mix = auto_full_temp_mix.TempMix(host, user, passwd, serial_port, baudrate)
        self.temp_read = auto_full_temp_read.TempRead(host, user, passwd, serial_port, baudrate)
        self.temp_write = auto_full_temp_write.TempWrite(host, user, passwd, serial_port, baudrate)
        self.bw_mix = auto_MS_aver_BW_mix.BwMix(host, user, passwd, serial_port, baudrate)
        self.bw_seq_read = auto_MS_aver_BW_seq_read.BwRead(host, user, passwd, serial_port, baudrate)
        self.bw_seq_write = auto_MS_aver_BW_seq_write.BwWrite(host, user, passwd, serial_port, baudrate)

if __name__ == '__main__':
    run_script = raw_input("please enter you want to run script(full_temp_mix or full_temp_read "
                       "or full_temp_write or bw_mix or bw_read or bm_write): ")

    run = RunScriptt("172.29.130.204", 'cnex', 'nvme')
    if run_script == "full_temp_mix" :
        pwm_set = int(raw_input("please enter you want set pwm value (50 or other value): "))
        run.temp_mix.set_pwm(pwm_set)
        temp_set = int(raw_input("please enter you want set temperature value: "))
        run.temp_mix.temp_value = temp_set
        pr_write = raw_input("Do you want to precondition (y or n): ")
        if pr_write.lower() == "y":
            run.temp_mix.pre_write()
            run.temp_mix.temp_run_test()
        else:
            run.temp_mix.temp_run_test()
    elif run_script == "full_temp_read":
        pwm_set = int(raw_input("please enter you want set pwm value (50 or other value): "))
        run.temp_read.set_pwm(pwm_set)
        temp_set = int(raw_input("please enter you want set temperature value: "))
        run.temp_read.temp_value = temp_set
        pr_write = raw_input("Do you want to precondition (y or n): ")
        if pr_write.lower() == "y":
            run.temp_read.pre_write()
            run.temp_read.temp_run_test()
        else:
            run.temp_read.temp_run_test()
    elif run_script == "full_temp_write":
        pwm_set = int(raw_input("please enter you want set pwm value (50 or other value): "))
        run.temp_write.set_pwm(pwm_set)
        temp_set = int(raw_input("please enter you want set temperature value: "))
        run.temp_write.temp_value = temp_set
        pr_write = raw_input("Do you want to precondition (y or n): ")
        if pr_write.lower() == "y":
            run.temp_write.pre_write()
            run.temp_write.temp_run_test()
        else:
            run.temp_write.temp_run_test()
    elif run_script == "bw_mix":
        pwm_set = int(raw_input("please enter you want set pwm value (50 or other value): "))
        run.bw_mix.set_pwm(pwm_set)
        BW_set = int(raw_input("please enter you want set BW value : "))
        run.bw_mix.bw_value = BW_set
        pr_write = raw_input("Do you want to precondition (y or n): ")
        if pr_write.lower() == "y":
            run.bw_mix.pre_write()
            run.bw_mix.run_test()
        else:
            run.bw_mix.run_test()
    elif run_script == "bw_read":
        pwm_set = int(raw_input("please enter you want set pwm value (50 or other value): "))
        run.bw_seq_read.set_pwm(pwm_set)
        BW_set = int(raw_input("please enter you want set BW value : "))
        run.bw_seq_read.bw_value = BW_set
        pr_write = raw_input("Do you want to precondition (y or n): ")
        if pr_write.lower() == "y":
            run.bw_seq_read.pre_write()
            run.bw_seq_read.run_test()
        else:
            run.bw_seq_read.run_test()
    elif run_script == "bm_write":
        pwm_set = int(raw_input("please enter you want set pwm value (50 or other value): "))
        run.bw_seq_write.set_pwm(pwm_set)
        BW_set = int(raw_input("please enter you want set BW value : "))
        run.bw_seq_write.bw_value = BW_set
        pr_write = raw_input("Do you want to precondition (y or n): ")
        if pr_write.lower() == "y":
            run.bw_seq_write.pre_write()
            run.bw_seq_write.run_test()
        else:
            run.bw_seq_write.run_test()