#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/4/18 14:24
@filename:test_email2

"""
import os
import re
import smtplib
from email.utils import parseaddr, formataddr
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate



def _getIP(domain_name, name_server=""):
    temp_file = os.getenv("temp") + "\\temp.lsh"
    domain_name_file = os.system("nslookup -qt=a " + domain_name + " " + name_server + " >" + temp_file + " 2>&1")
    f = open(temp_file)
    c = f.read()
    print(c)
    f.close()
    os.remove(temp_file)
    ips = re.findall(domain_name + r"\s*Address\s*:\s*(\S+)", c, re.I)

    if ips:
        return ips[0][0]
    elif name_server == "":
        return _getIP(domain_name, "8.8.8.8")
    else:
        return None

def _get_internet_address(content):
    internet_addresses=re.findall(r"(\S+)\s+internet\s+address\s*=\s*(\S+)",content)
    internet_addresses_map={}
    for internet_address in internet_addresses:
        internet_addresses_map[internet_address[0]]=internet_address[1]
    return internet_addresses_map

def _send_to_mail_exchanger(mail_exchanger, mail_from, rcpt_to, From="", To="", Subject="", Date=None, Body="",
                            attachments=None, encoding="gbk"):


    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()
    # 设置根容器属性
    main_msg['From'] = From
    main_msg['To'] = To
    main_msg['Subject'] = Subject
    if Date:
        main_msg['Date'] = Date
    else:
        main_msg['Date'] = formatdate()

    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    text_msg = MIMEText(Body, 'html', encoding)
    main_msg.attach(text_msg)

    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    if attachments:
        for attachment in attachments:
            if not os.path.isfile(attachment):
                continue
            if IsImage(attachment):
                try:
                    fp = open(attachment, "rb")
                    file_msg = MIMEImage(fp.read())
                    fp.close()
                    file_msg.add_header("Content-ID",
                                        os.path.basename(attachment).replace(".jpg", "").replace(".png", ""))
                    main_msg.attach(file_msg)
                except:
                    pass
            else:
                file_msg = MIMEBase("application", "octet-stream")
                f = open(attachment, 'rb')
                file_msg.set_payload(f.read())
                f.close()
                email.encoders.encode_base64(file_msg)
                file_msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment))
                main_msg.attach(file_msg)

    # 用smtp发送邮件
    data = main_msg.as_string()
    for i in range(2):
        try:
            # Log(mail_exchanger)
            server = smtplib.SMTP(mail_exchanger)
            # Log(mail_from)
            # Log(rcpt_to)
            ret = server.sendmail(mail_from, rcpt_to, data)
            break
        except:
            import traceback
            # Log(traceback.format_exc())
            ret = False
            try:
                server.quit()
            except:
                pass
    try:
        server.quit()
    except:
        pass

    if ret == False or ret:
        # print "发往如下的邮件失败:",rcpt_to
        return False
    return True

def _get_mail_exchanger(domain_name, name_server=""):
    # print domain_name
    temp_file = os.getenv("temp") + "\\temp.lsh"
    os.system("nslookup -qt=mx " + domain_name + " " + name_server + " >" + temp_file + " 2>&1")
    f = open(temp_file)
    c = f.read()
    f.close()
    os.remove(temp_file)
    # print c
    internet_addresses_map = _get_internet_address(c)
    mail_exchangers = re.findall(r"mail\s+exchanger\s*=\s*(\S+)", c)
    # mail_exchangers=[internet_addresses_map.get(i,i) for i in mail_exchangers]
    mail_exchangerIPs = []
    for i in mail_exchangers:
        try:
            mail_exchangerIPs.append(internet_addresses_map[i])
        except:
            ip = _getIP(i)
            if ip:
                mail_exchangerIPs.append(ip)

    if mail_exchangerIPs or name_server:
        print("mail_exchangers", mail_exchangerIPs)

        return mail_exchangerIPs
    else:
        print("mail_exchangers from 预配置", g_mail_exchanger.get(domain_name, []))
        return g_mail_exchanger.get(domain_name, [])

print(_getIP("www.baidu.com"))