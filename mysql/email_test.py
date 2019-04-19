#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/4/18 11:35
@filename:email_test

"""
#coding:utf-8
from socket import *
msg = b"\r\n I love computer networks!"   #需要发送的数据
endmsg = b"\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("163mx02.mxmail.netease.com",25)  #Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# #Fill in end
recv = clientSocket.recv(1024)
print('recv:',recv)
print(type(recv[:3]))
if recv[:3] != b'220':
    print('220 reply not received from server.')
# # Send HELO command and print server response.
heloCommand = b'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print('recv1:',recv1)
if recv1[:3] != b'250':
    print('250 reply not received from server.')
#
# # Send MAIL FROM command and print server response.
# # Fill in start
fromCommand = b"MAIL FROM:<system@net.cn>\r\n"  #匿名邮件的「发送人」，可以随意伪造
clientSocket.send(fromCommand)
recv2 = clientSocket.recv(1024)
print ('recv2:', recv2)
# # Fill in end
# # Send RCPT TO command and print server response.
# # Fill in start b"RCPT TO:<13750842560@163.com>\r\n"
toCommand = b"RCPT TO:<13750842560@163.com>\r\n"   #收件人地址。
clientSocket.send(toCommand)
recv3 = clientSocket.recv(1024)
print ('recv3:', recv3)
# # Fill in end
# # Send DATA command and print server response.
# # Fill in start
dataCommand = b"DATA\r\n"
clientSocket.send(dataCommand)
recv4 = clientSocket.recv(1024)
print('recv4:', recv4)
# Fill in end
# Send message data.
# Fill in start
clientSocket.send(msg)
# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg)
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitCommand = b"QUIT\r\n"
clientSocket.send(quitCommand)
recv5 = clientSocket.recv(1024)
print('recv5:', recv5)
# Fill in end
clientSocket.close()