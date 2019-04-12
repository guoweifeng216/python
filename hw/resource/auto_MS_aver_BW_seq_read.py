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
import getpass
import subprocess as sub
from optparse import OptionParser


class BwRead(object):
    def __init__(self, host, user, passwd, serial_port ='COM4',baudrate = 9600 ):    #PWM控制器串口设置
        """dd"""
        self.pwm = 45                                                                #初始PWM占空比值
        self.remote_copy_path = "D:\wfguo\copy"
        self.local_file_path = r"C:\Users\{}\Desktop\IOmeter-free\Iometer_with_log\Results".format(getpass.getuser())
        self.cmd_path = r"C:\Users\{}\Desktop\IOmeter-free\Iometer_with_log".format(getpass.getuser())
        self.host = host
        self.user = user
        self.passwd = passwd
        self.aver = r"%s\%s"% (self.local_file_path, "aver.csv")
        self.input_name = "*log.csv"
        self.aver_value = 0
        self.bw_value = 0
        self.remove_file()
        self.serialPort = serial_port  # 串口
        self.baudRate = baudrate  # 波特率

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
        read_file = "IOMeter_seq_read.bat"                                    #每跑三分钟计算平均性能所用的脚本
        read_cmd = "{}\{}".format(self.cmd_path, read_file)
        run_cmd = sub.call(read_cmd, shell=True)
        if run_cmd != 0:
            print("run iometer failed")

    def local_run_iometer_15m(self):
        read_file = "IOMeter_seq_read_15m.bat"                                #稳定后跑15分钟所用的脚本
        read_cmd = "{}\{}".format(self.cmd_path, read_file)
        run_cmd = sub.call(read_cmd, shell=True)
        if run_cmd != 0:
            print("run iometer failed")

    def seq_read_date_15m(self):
        self.local_run_iometer_15m()
        self.average_bw()
        print("The pwm have stability,then run 15m,it's average seq read value:{}".format(self.aver_value))

    def pre_write(self):
        pre_write_file = "IOMeter_128KB_Seq_write_precondition.bat"           #预埋用的脚本，需加入指令“--pre_wr 1”
        pre_cmd = "{}\{}".format(self.cmd_path, pre_write_file)
        run_cmd = sub.call(pre_cmd, shell=True)
        if run_cmd != 0:
            print("iometer pre write failed")

    def average_bw(self,):                                                    #计算IOmeter result log平均性能所用的脚本
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
        csv_out_file.close()

    def set_pwm(self, pwm):
        ser = serial.Serial(self.serialPort, self.baudRate, timeout=0.5)
        print("Set the pwm value :{}".format(pwm))
        self.pwm = pwm
        ser.write('D1:%03d' % pwm)
        ser.close()

    def run_test(self):
        self.local_run_iometer()
        self.average_bw()
        pwm = self.pwm
        while True:
            time.sleep(2)
            print("you have been access auto adjust......")
            print("The current average value:{}".format(self.aver_value))
            tmp = float(self.aver_value) - self.bw_value                                                             #性能比较数值为1600MiB/s
            print("The set value {} minus average value {} equal : {}".format(1600, self.aver_value, tmp))
            if (tmp >= -50) and (tmp <= 50):
                print("The pwm value is normal,it's: {}".format(pwm))
                self.seq_read_date_15m()
                break
            elif tmp > 100:
                print("the current pwm value {},please decrease the pwm value".format(pwm))
                pwm -= 5
                self.set_pwm(pwm)
                self.local_run_iometer()
                self.average_bw()
            elif tmp < -100:
                print("the current pwm value {},please increase the pwm value".format(pwm))
                pwm += 5
                self.set_pwm(pwm)
                self.local_run_iometer()
                self.average_bw()
            elif (tmp > 50) and (tmp <= 100):
                print("the current pwm value {},please decrease the pwm value".format(pwm))
                pwm -= 1
                self.set_pwm(pwm)
                self.local_run_iometer()
                self.average_bw()
            elif (tmp >= -100) and (tmp < -50):
                print("the current pwm value {},please increase the pwm value".format(pwm))
                pwm += 1
                self.set_pwm(pwm)
                self.local_run_iometer()
                self.average_bw()
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
#         run.run_test()
#     else:
#         run.seq_read_date_15m()
