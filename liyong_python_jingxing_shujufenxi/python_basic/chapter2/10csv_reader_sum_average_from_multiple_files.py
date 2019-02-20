#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/7 9:48
@filename:10csv_reader_sum_average_from_multiple_files

"""
import csv
import glob
import os
import sys
input_path = sys.argv[1]
output_file = sys.argv[2]
# output_header_list = ['filename', 'total_sales', 'average_sales']
output_header_list = ['filename', 'Total MBs per Second', 'average']
csv_out_file = open(output_file, 'w', newline='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)
for input_file in glob.glob(os.path.join(input_path,'128K_Seq_Reads_QD128_2H.log*')):
    with open(input_file, 'r',newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(filereader)
        total_sales = 0.0
        number_of_sales = 0.0
        for row in filereader:
            sale_amount = row[1]
            total_sales += float(str(sale_amount))
            # total_sales += float(str(sale_amount).strip('$').replace(',', ''))
            number_of_sales += 1

        average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        print(output_list)
        filewriter.writerow(output_list)
csv_out_file.close()