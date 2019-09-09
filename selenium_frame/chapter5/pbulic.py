#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/9/2 14:12
filename:   pbulic
"""


class Login():
    def __init__(self):
        pass

    def user_login(self, driver, username, password):
        print('start login---------')
        driver.find_element_by_id("idInput").clear()
        driver.find_element_by_id("idInput").send_keys(username)
        driver.find_element_by_id("pwdInput").clear()
        driver.find_element_by_id("pwdInput").send_keys(password)
        driver.find_element_by_id("loginBtn").click()

    def user_logout(self, driver):
        print('start logout---------')
        driver.find_element_by_id("退出").click()
        driver.quit()