#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
smtpserver = 'https://outlook.office.com'
user = 'weifeng.guo@cnexlabs.com'
password = 'ZXcv.0123'
sender =  'weifeng.guo@cnexlabs.com'
receiver = '782388110@qq.com'
subject = 'python email test'
msg = MIMEText('<html><h1>你好</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
