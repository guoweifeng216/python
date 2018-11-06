#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/9/6 11:09
@filename:practice
"""
strings = raw_input("请输入字符串：")
print("输入的字符串：%s" % strings)
fp = open('text.txt', 'w')
strings = strings.upper()
fp.write(strings)
fp.close()
print("转换后的字符串：%s" % strings)
