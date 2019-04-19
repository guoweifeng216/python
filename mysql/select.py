#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/4/16 14:17
@filename:select

"""
import MySQLdb
import sys

sql="desc db1.t1"

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","db1" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchall()

for i in data:
    # print(i)
    for j in i:
            sys.stdout.write(str(j)+'\t')
    sys.stdout.write('\n')


# 关闭数据库连接
db.close()