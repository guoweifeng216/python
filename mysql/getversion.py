#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/4/16 13:45
@filename:getversion

"""
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "db1")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
