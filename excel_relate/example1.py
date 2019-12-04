#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/9/9 15:05
filename:   example1
"""
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline
# %config InlineBackend.figure_format = 'wvg'
# plt.rcParams['front.sans-serif'] = 'SimHei'
# plt.rcParams['axes.unicode_minus'] = False
test_list = [1, 2, 3, 4, 5]
test_list2 = ['a', 'b', 'c', 'd', 'e']
test_list3 = [['a', 'A'],['b', 'B'], ['c', 'C'], ['d', 'D']]
data_dict = {"小写":['a', 'b', 'c', 'd'], "大写":['A', 'B', 'C', 'D']}
# s1 = pd.Series(test_list)
# print(s1)
# s2 = pd.Series(test_list, index= ['a', 'b', 'c', 'd', 'e'])
# print(s2)
#
# s3 = pd.Series({'a':1, 'b':2, 'c':3, 'd':4})
# print(s3)
# print(s1.index)
# print(s2.index)
# print(s1.values)
# print(s2.values)
df1 = pd.DataFrame(test_list2)
# print(df1)
df2 = pd.DataFrame(test_list3, columns = ['小写', '大写'], index=['一', '二', '三', '四'])
# print(df2)
df3 = pd.DataFrame(data_dict, index=['一', '二', '三', '四'])
# print(df3)

excel_data = pd.read_excel(r'E:\github\python\excel_relate\exampl1.xlsx', index_col=0)
print(excel_data)
# print(excel_data.shape)
# print(excel_data.info())
# print(excel_data.describe())
# print(excel_data.dropna(how ='all'))  # 删除空白行
# print(excel_data.fillna(0))  # 所有缺失项填0
# print(excel_data.fillna({'性别': '男'}))  # 补缺特定列的缺失值
# print(excel_data['年龄'].astype('float64'))  # 转换年龄列的数据类型
print(excel_data.iloc[:,[0,2]]) #iloc后的方括号中逗号之前部分表示要获取的行的位置，只输入一个冒号，不输入任何数值表示获取所有的行，逗号之后表示获取列的位置，从0开始计数
print(excel_data.iloc[:,0:2])
# excel_data.to_excel(excel_writer=r'E:\github\python\excel_relate\exampl4.xlsx', encoding='utf-8', index=False)
# fig = plt.figure(figsize=(8, 6))
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# plt.show()

x = np.arange(6)
y = np.arange(6)
plt.subplot2grid((2, 2), (0, 0))
plt.plot(x, y)

plt.subplot2grid((2, 2), (0, 1))
plt.bar(x, y)
plt.show()
