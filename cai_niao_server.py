#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/9/5 16:42
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print host
port = 12345
# s.bind(host, 8002)
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print "连接地址", addr
    c.send("欢迎访问")
    c.close()
