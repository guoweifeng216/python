#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/4 16:21
@filename:9csv_reader_concat_rows_from_multiple_files

"""
import sys
import os
import csv
import glob
input_path = sys.argv[1]
output_file = sys.argv[2]
file_first = True
for input_file in glob.glob(os.path.join(input_path, 'supplier*.csv')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewrite = csv.writer(csv_out_file)
            if file_first:
                for row in filereader:
                    filewrite.writerow(row)
                file_first = False
            else:
                header = next(filereader)
                for row in filereader:
                    filewrite.writerow(row)
