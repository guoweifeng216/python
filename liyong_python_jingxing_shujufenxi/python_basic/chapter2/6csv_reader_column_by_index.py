#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/4 10:56
@filename:6csv_reader_column_by_index

"""
import sys
import re
import csv
input_file = sys.argv[1]
output_file = sys.argv[2]
my_columns = [0, 3]
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewrite = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_out = []
            for index_value in my_columns:
                row_list_out.append(row_list[index_value])
                filewrite.writerow(row_list_out)
