#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/7/5 14:10
@filename:time_sub

"""

import datetime
import time


def datetime_toString(dt):
    """把datetime转成字符串"""
    return dt.strftime("%Y-%m-%d")


def string_toDatetime(string):
    """把字符串转成datetime"""
    return datetime.datetime.strptime(string, "%Y-%m-%d")


def string_toTimestamp(strTime):
    """把字符串转成时间戳形式"""
    return time.mktime(string_toDatetime(strTime).timetuple())


def timestamp_toString(stamp):
    """把时间戳转成字符串形式"""
    return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))


def datetime_toTimestamp(dateTime):
    """把datetime类型转外时间戳形式"""
    return time.mktime(dateTime.timetuple())


def substract_DateTime(dateStr1, dateStr2):
    """ 返回两个日期之间的差 """
    d1 = string_toDatetime(dateStr1)
    d2 = string_toDatetime(dateStr2)
    return d2 - d1


def substract_TimeStamp(dateStr1, dateStr2):
    """ 两个日期的 timestamp 差值 """
    ts1 = string_toTimestamp(dateStr1)
    ts2 = string_toTimestamp(dateStr2)
    return ts1 - ts2


def compare_dateTime(dateStr1, dateStr2):
    """两个日期的比较, 当然也可以用timestamep方法比较,都可以实现."""
    date1 = string_toDatetime(dateStr1)
    date2 = string_toDatetime(dateStr2)
    return date1.date() > date2.date()


def dateTime_Add(dateStr, days=0, hours=0, minutes=0):
    """ 指定日期加上 一个时间段，天，小时，或分钟之后的日期 """
    date1 = string_toDatetime(dateStr)
    return date1 + datetime.timedelta(days=days, hours=hours, minutes=minutes)


if __name__ == '__main__':
    print(substract_DateTime('2012-12-12', '2012-01-01'))
    # -346 days, 0:00:00
    print(substract_DateTime('2012-12-12', '2012-01-01').days)
