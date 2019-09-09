#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/9/2 14:14
filename:   mailtest
"""
from selenium import webdriver
from  pbulic import Login


class LoginTest():

    def __init__(self):
        self.email_addr = "https://mail.163.com/"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(self.email_addr)

    def test_admin_login(self):
        user_name = 'admin'
        password = '123'
        Login.user_login(self.driver, user_name, password)
        self.driver.quit()

    def test_user_login(self):
        user_name = 'guest'
        password ='123'
        Login.user_login(self.driver, user_name, password)
        self.driver.quit()


LoginTest.test_admin_login()

LoginTest.test_user_login()