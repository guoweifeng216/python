#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

@athor:weifeng.guo 
@data:2019/1/10 18:47
@filename:login

"""
import os
import time
import sys
import csv
import glob
import serial
import shutil
import re
import getpass
import threading
import subprocess as sub
from optparse import OptionParser
import multiprocessing


class TempWrite(object):
    def __init__(self, host, user, passwd, serial_port ='COM4',baudrate = 9600 ):
        """dd"""
        self.pwm = 50
        self.result = False
        self.remote_copy_path = "D:\wfguo\copy"
        self.local_file_path = r"C:\Users\{}\Desktop\IOmeter-free\Iometer_with_log\Results".format(getpass.getuser())
        self.cmd_path = r"C:\Users\{}\Desktop\IOmeter-free\Iometer_with_log".format(getpass.getuser())
        self.host = host
        self.user = user
        self.passwd = passwd
        self.aver = r"%s\%s"% (self.local_file_path, "aver.csv")
        self.input_name = "*log.csv"
        self.aver_value = 0
        self.remove_file()
        self.serialPort = serial_port  # 串口
        self.baudRate = baudrate  # 波特率
        self.temp_value = 0

    def remove_file(self):
        if os.path.exists(self.remote_copy_path):
            shutil.rmtree(self.remote_copy_path)

    def remote_run_iometer_copy_file(self):
        run_cmd = r"%sPsExec64.exe -u %s -p %s \\%s -s -d -i %s" % (os.path.dirname(__file__), self.user,self.passwd, self.host,self.cmd_path)
        print(run_cmd)
        run_res = sub.call(run_cmd, shell=True)
        print(run_res)
        print("run_res value is %s" % run_res)
        copy_path = r"net use \\%s\C$ %s /user:%s " % (self.host,self.passwd,self.user)
        copy_cmd = r"xcopy \\{}\c\Users\cnex\Desktop\iometer {}\ ".format(self.host,self.copy_path)
        # print(copy_cmd)
        copy_ret = sub.call(copy_path, shell=True)
        if copy_ret != 0:
            print("Connection Fail")
        else:
            run_copy_ret = sub.call(copy_cmd, shell=True)
            if run_copy_ret != 0:
                print("Copy Fail")

    def local_run_iometer(self):
        read_file = "IOMeter_128KB_Seq_write_QD128_2H.bat"
        read_cmd = "{}\{}".format(self.cmd_path, read_file)
        print("******run Iometer*****")
        run_cmd = sub.call(read_cmd, shell=True)
        if run_cmd != 0:
            print("run iometer failed")

    def pre_write(self):
        pre_write_file = "IOMeter_128KB_Seq_write_precondition.bat"
        pre_cmd = "{}\{}".format(self.cmd_path, pre_write_file)
        run_cmd = sub.call(pre_cmd, shell=True)
        if run_cmd != 0:
            print("iometer pre write failed")

    def average_bw(self,):
        output_header_list = ['filename', 'Total MBs per Second', 'average']
        if sys.version >= '3':
            csv_out_file = open(self.aver, 'w', newline='')
        else:
            csv_out_file = open(self.aver, 'wb')

        filewriter = csv.writer(csv_out_file)
        filewriter.writerow(output_header_list)
        # average_BW = 0
        for input_file in glob.glob(os.path.join(self.local_file_path, self.input_name)):
            if sys.version >= '3':
                with open(input_file, 'r', newline='') as csv_in_file:
                    filereader = csv.reader(csv_in_file)
                    output_list = []
                    output_list.append(os.path.basename(input_file))
                    header = next(filereader)
                    total_BW = 0.0
                    number_of_time = 0.0
                    for row in filereader:
                        sale_amount = row[1]
                        total_BW += float(str(sale_amount))
                        number_of_time += 1

                    average_BW = '{0:.2f}'.format(total_BW / (number_of_time - 2))
                    output_list.append(total_BW)
                    output_list.append(average_BW)
                    # print(output_list)
                    filewriter.writerow(output_list)
                    self.aver_value = average_BW
            else:
                with open(input_file, 'r') as csv_in_file:
                    filereader = csv.reader(csv_in_file)
                    output_list = []
                    output_list.append(os.path.basename(input_file))
                    header = next(filereader)
                    total_BW = 0.0
                    number_of_time = 0.0
                    for row in filereader:
                        sale_amount = row[1]
                        total_BW += float(str(sale_amount))
                        number_of_time += 1

                    average_BW = '{0:.2f}'.format(total_BW / (number_of_time - 2))
                    output_list.append(total_BW)
                    output_list.append(average_BW)
                    # print(output_list)
                    filewriter.writerow(output_list)
                    self.aver_value = average_BW
        print("The average of BW value:{}".format(self.aver_value))
        csv_out_file.close()

    def set_pwm(self, pwm):
        ser = serial.Serial(self.serialPort, self.baudRate, timeout=0.5)
        print("Set the pwm value :{}".format(pwm))
        self.pwm = pwm
        ser.write('D1:%03d' % pwm)
        ser.close()

    def set_disable(self):
        ser = serial.Serial('COM5', 921600, timeout=0.5)
        ser.write('therctr 0' + '\n')
        result = ser.readlines()
        print(result[2])
        ser.close()

    def acquire_temp(self):
        ser = serial.Serial('COM5', 921600, timeout=0.5)
        ser.write(('temp' + '\n').encode())
        result_list = ser.readlines()
        current_temp = int(re.findall(r'\d+', result_list[2])[0])
        print("The current temperature:{}".format(current_temp))
        ser.close()
        return current_temp

    def temp_run_test(self):
        process_run_iometer = multiprocessing.Process(target=self.local_run_iometer)
        process_check_temp = multiprocessing.Process(target=self.check_temp)
        process_run_iometer.start()
        process_check_temp.start()
        process_run_iometer.join()
        process_check_temp.join()

    def check_temp(self):
        print("**********check temp*****")
        pwm = self.pwm
        counter_temp = 0
        while True:
            time1 = time.time()
            time.sleep(10)
            time2 = time.time()
            print('counter time {}'.format(time2-time1))
            temp = self.acquire_temp()
            temp_value = temp - self.temp_value
            print("The target temp  value {} ,the delta temp value: {}".format(114, temp_value))
            if (temp_value >= -2) and (temp_value <= 2):
                print("The temp value is normal,it's: {}".format(self.acquire_temp()))
                counter_temp +=1
                print("the current counter_temp value {}".format(counter_temp))
                if counter_temp ==30:
                    break
                else:
                    pass
                    
            elif temp_value > 4:
                print("the current pwm value {},please increase the pwm value".format(pwm))
                pwm += 3
                self.set_pwm(pwm)
                counter_temp = 0
            elif temp_value < -6:
                print("the current pwm value {},please decrease the pwm value".format(pwm))
                pwm -= 2
                self.set_pwm(pwm)
                counter_temp = 0
            elif (temp_value > 2) and (temp_value <= 4):
                print("the current pwm value {},please increase the pwm value".format(pwm))
                pwm += 1
                self.set_pwm(pwm)
                counter_temp = 0
            elif (temp_value >= -6) and (temp_value < -2):
                print("the current pwm value {},please decrease the pwm value".format(pwm))
                pwm -= 1
                self.set_pwm(pwm)
                counter_temp = 0
            else:
                print("please manual adjust")

# if __name__ == '__main__':
#     optparser = OptionParser()
#     optparser.add_option("--host", type=str, dest="host", default="172.29.131.8", help="host name")
#     optparser.add_option("--pre_wr", type=str, dest="pre_wr", default=False, help="pre_write")
#     optparser.add_option("--read", type=str, dest="read", default=False, help="read")
#     (options, args) = optparser.parse_args()
#
#     host = options.host
#     pre_write = options.pre_wr
#     read_enable = options.read
#     run = Process(host, 'cnex', 'nvme')
#     if not read_enable:
#         run.temp_run_test()
#     else:
#         run.seq_read_date_15m()
