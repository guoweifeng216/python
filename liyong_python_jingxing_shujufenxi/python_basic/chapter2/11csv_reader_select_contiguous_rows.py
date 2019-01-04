#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/4 14:46
@filename:11csv_reader_select_contiguous_rows

"""
import sys
import csv
input_file = sys.argv[1]
output_file = sys.argv[2]
row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewrite = csv.writer(csv_out_file)
        for row_list in filereader:
            if (row_counter >= 3) and (row_counter <= 15):
                filewrite.writerow([value.strip() for value in row_list])
            row_counter +=1