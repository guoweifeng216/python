#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/3 19:13
@filename:2csv_reader_parsing_and_write

"""
import sys
import csv
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r', newline='', encoding='UTF-8') as csv_in_file:
    with open(output_file, 'w', newline='', encoding='UTF-8') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            print(row_list)
            filewriter.writerow(row_list)