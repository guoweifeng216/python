#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/9/5 16:46
"""
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
print s.recv(1024)
s.close()
