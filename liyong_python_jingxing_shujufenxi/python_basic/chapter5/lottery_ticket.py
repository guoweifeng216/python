#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/24 14:28
@filename:lottery_ticket

"""
import sys
import random
from optparse import OptionParser

input_file = sys.argv[1]
list_num = sys.argv[2]


def write_file(input_file,list_num):
    list_tmp =[]
    with open(input_file,'r+') as write_file:
        file_input = write_file.readlines()
        for num in file_input:
            list_tmp.append(num.strip('\n'))
        list_number = list_num.split(" ")
        for num in list_number:
            if num in list_tmp:
                pass
            else:
                print("add new number {} to the file".format(num))
                write_file.write(num + '\n')


def generate_number(input_file):
    with open(input_file,'r+') as read_file:
        read_num_list = read_file.readlines()
        list_tmp = []
        for num in read_num_list:
            list_tmp.append(num.strip('\n'))
        print("generate new six number {}".format(random.sample(list_tmp,6)))

write_file(input_file,list_num)
generate_number(input_file)