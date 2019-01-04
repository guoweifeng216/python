#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/1/3 11:04
@filename:pie_chart

"""
# -*- coding: utf-8 -*-
import xlrd
import sys
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime
# from pandas import Series, DataFrame

# labels = 'a', 'b', 'c', 'd'
#
# sizes = 5, 6, 7, 8
#
# colors = 'lightgreen', 'gold', 'lightskyblue', 'lightcoral'
#
# explode = 0, 0, 0, 0
#
# plt.pie(sizes, explode=explode, labels=labels,
#
#         colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
#
# plt.axis('equal')
#
# plt.show()

# data = xlrd.open_workbook('xuesheng.xlsx') # 打开xls文件
# table = data.sheets()[0] # 打开第一张表
# nrows = table.nrows      # 获取表的行数

# for i in range(len(data.sheets())):
#     table = data.sheets()[i]
#     nrows = table.nrows
#     colus = table.ncols
#     for j in range(nrows):   # 循环逐行打印
#         dict = {}
#         sum = 0
#         if j == 0:  # 跳过第一行
#             continue
#         for k in range(colus):
#             if k <= 1:
#                 continue
#             # print(table.row_values(j)[k])
#             sum += table.row_values(j)[k]
#         dict[j] = sum
#         print(dict)

df = pd.DataFrame(pd.read_excel('地理学生成绩.xls'))
# 查看数据表的维度
print(df.shape)

#  数据表信息
print(df.info())

# 查看数据表各列格式
print(df.dtypes)

# 检查数据空值
# print(df.isnull())

#查看数据表的值
# print(df.values)

#查看列名称

print(df.columns)

#查看前3行数据
# print(df.head(3))

#查看最后3行
# print(df.tail(3))
#更改数据格式
# print(df['总分'].astype('int'))
input_file = sys.argv[1]
print(input_file)