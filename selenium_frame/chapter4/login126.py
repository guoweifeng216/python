#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/8/29 14:22
filename:   login126
"""
import time
from selenium import webdriver

email_addr = "https://mail.163.com/"
driver = webdriver.Chrome()
driver.get(email_addr)
print('Before login---------')
title = driver.title
print(title)
now_url = driver.current_url
print(now_url)
driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("username")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("password")
driver.find_element_by_id("loginBtn").click()
time.sleep(5)
user = driver.find_element_by_id('spnUid').text
print(user)
print('After login------')
title = driver.title
print(title)
now_url = driver.current_url
print(now_url)
# driver.quit()