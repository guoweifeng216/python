#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/4 15:21
@filename:12csv_reader_add_header_row

"""
import sys
import csv
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewrite = csv.writer(csv_out_file)
        header_list = ['Supplier Name', 'Invoice Number','Part Number', 'Cost', 'Purchase Date']
        filewrite.writerow(header_list)
        for row_list in filereader:
            filewrite.writerow(row_list)