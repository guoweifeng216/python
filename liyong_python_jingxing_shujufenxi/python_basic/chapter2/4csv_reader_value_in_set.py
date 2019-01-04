#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/4 10:18
@filename:4csv_reader_value_in_set

"""
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
important_dates = ['1/20/14', '1/30/14']
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewrite = csv.writer(csv_out_file)
        header = next(filereader)
        filewrite.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewrite.writerow(row_list)
