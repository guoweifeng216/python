#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/4/18 14:01
@filename:test_email

"""
# coding=UTF-8

import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['From'] = '13750842560@163.com'
msg['To'] = '13750842560@163.com'
msg['subject'] = 'test'
content = '''
       你好:
            这是一封自动发送的邮件。
            '''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib.SMTP('smtp.163.com', '25')
#打开调试信息
smtp.set_debuglevel(True)
#连接服务器
smtp.starttls()
#登录服务器
smtp.login('13750842560@163.com', 'guoweifeng0216')
#发送邮件
smtp.sendmail('13750842560@163.com', '13750842560@163.com', msg.as_string())
smtp.quit()
