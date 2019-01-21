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
import subprocess as sub
from optparse import OptionParser

class Process(object):
    def __init__(self, host, user, passwd, serial_port ='COM4',baudrate = 9600 ):
        """dd"""
        self.pwm = 35
        self.remote_copy_path = "D:\wfguo\copy"
        self.local_file_path = r"C:\Users\cnex\Desktop\IOmeter-free\Iometer_with_log\Results"
        self.cmd_path = r"C:\Users\cnex\Desktop\IOmeter-free\Iometer_with_log\IOMeter_seq_read.bat"
        self.host = host
        self.user = user
        self.passwd = passwd
        self.aver = r"%s\%s"% (self.local_file_path, "aver.csv")
        self.input_name = "*log.csv"
        self.aver_value = 0
        self.remove_file()
        self.serialPort = serial_port  # 串口
        self.baudRate = baudrate  # 波特率

    def remove_file(self):
        if os.path.exists(self.remote_copy_path):
            shutil.rmtree(self.remote_copy_path)
    def CountDown(self, sec):
        print("%d seconds count down start:" % sec)
        while sec:
            mins, secs = divmod(sec, 60)
            count_down = '{:02d}:{:02d}'.format(mins, secs)
            # print(count_down, end  = '\r')
            time.sleep(1)
            sec -= 1

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
        run_cmd = sub.call(self.cmd_path, shell=True)
        if run_cmd != 0:
            print("run iometer failed")

    def CheckMachine(self, host, msg):
        print(">>>>>>>>  %s  <<<<<<<<" % msg)
        fail_count = 1
        success_count = 0
        cmd = 'ping -n 2 %s' % host

        while fail_count <= 30:

            time.sleep(5)
            print("\n -------------------------------------------------------------")
            print("\n# Start Ping: # %d    Time: %s \n " % (fail_count, str(time.ctime())))
            p = sub.Popen(cmd, shell=True, stdin=sub.PIPE, stdout=sub.PIPE, stderr=sub.PIPE)
            stdoutdata, stderrdata = p.communicate()
            print(stdoutdata)
            ping_result = stdoutdata.decode('gbk', 'ignore')

            if '(0% loss)' in ping_result or \
                    (u'无法访问目标主机' not in ping_result and u'(0% 丢失)' in ping_result):
                print("------> Ping Succeed, Test Still Running...........\n")
                fail_count = 1
                success_count += 1
                if success_count >= 30:
                    print("Sanity test has finished, Auto stop the test!")
                    sys.exit(0)
            else:
                print("------> Ping Failed\n")
                fail_count += 1
                success_count = 0
        else:
            res_ping = 1
        return res_ping

    def average_bw(self,):
        output_header_list = ['filename', 'Total MBs per Second', 'average']
        if sys.version >= '3':
            csv_out_file = open(self.aver, 'w', newline='')
        else:
            csv_out_file = open(self.aver, 'wb')

        filewriter = csv.writer(csv_out_file)
        filewriter.writerow(output_header_list)
        average_sales = 0
        for input_file in glob.glob(os.path.join(self.local_file_path, self.input_name)):
            if sys.version >= '3':
                with open(input_file, 'r', newline='') as csv_in_file:
                    filereader = csv.reader(csv_in_file)
                    output_list = []
                    output_list.append(os.path.basename(input_file))
                    header = next(filereader)
                    total_sales = 0.0
                    number_of_sales = 0.0
                    for row in filereader:
                        sale_amount = row[1]
                        total_sales += float(str(sale_amount))
                        number_of_sales += 1

                    average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
                    output_list.append(total_sales)
                    output_list.append(average_sales)
                    # print(output_list)
                    filewriter.writerow(output_list)
                    self.aver_value = average_sales
            else:
                with open(input_file, 'r') as csv_in_file:
                    filereader = csv.reader(csv_in_file)
                    output_list = []
                    output_list.append(os.path.basename(input_file))
                    header = next(filereader)
                    total_sales = 0.0
                    number_of_sales = 0.0
                    for row in filereader:
                        sale_amount = row[1]
                        total_sales += float(str(sale_amount))
                        number_of_sales += 1

                    average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
                    output_list.append(total_sales)
                    output_list.append(average_sales)
                    # print(output_list)
                    filewriter.writerow(output_list)
                    self.aver_value = average_sales
        csv_out_file.close()
        return average_sales

    def set_pwm(self):
		ser = serial.Serial(self.serialPort, self.baudRate, timeout=0.5)
        # pwd = input("please enter you want to set number: ")
		ser.write('D1:050')
		#ser.write('D1:020')
		#print(ser.write('read'))  # 可以接收中文
		ser.close()

    def run_test(self):
        # self.local_run_iometer()
        aver_value = self.average_bw()

        n = 0
        while n < 5:
            #print(aver_value)
            tmp = float(aver_value) - 1600
            #print(tmp)
            #print(self.pwm)
            if (tmp >= -50) and (tmp <= 50):
                pwm = serial.Serial(self.serialPort, self.baudRate, timeout=0.5).readline()
                print("The pwm value is normal {}".format(pwm))
                break
            elif tmp > 100:
                #self.pwm -= 5
                #self.set_pwm(self.pwm)
                # self.remove_file()
                # self.local_run_iometer()
                self.average_bw()
            elif tmp < -100:
                #self.pwm += 5
                self.set_pwm()
                # self.remove_file()
                # self.local_run_iometer()
                self.average_bw()
            elif (tmp > 50) and (tmp <= 100):
                #self.pwm -= 2
                self.set_pwm(self.pwm)
                self.remove_file()
                # self.local_run_iometer()
                self.average_bw()
            elif (tmp >= -100) and (tmp < -50):
                #self.pwm += 2
                self.set_pwm(self.pwm)
                self.remove_file()
                # self.local_run_iometer()
                self.average_bw()
            else:
                print("please manual adjust")
            n += 1


if __name__ == '__main__':
    optparser = OptionParser()
    optparser.add_option("--host", type=str, dest="host", default="172.29.131.8", help="host name")
    (options, args) = optparser.parse_args()

    host = options.host

    run = Process(host, 'cnex', 'nvme')
    run.run_test()
    # run.average_bw()
