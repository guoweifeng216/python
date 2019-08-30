#!/usr/bin/env python
# coding=utf-8
"""
author:     weifeng.guo 
data:       2019/8/29 14:51
filename:   mouse
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

first = "http:www.baidu.com"

driver = webdriver.Chrome()
driver.get(first)
# 模拟右击
right_click = driver.find_element_by_id('su')
# ActionChains(driver).context_click(right_click).perform()

# 模拟悬停
above = driver.find_element_by_id('id')
# ActionChains(driver).move_to_element(above).perform()

# 模拟双击
double_click = driver.find_element_by_id('su')
ActionChains(driver).double_click(double_click).perform()

# 模式拖放
element = driver.find_element_by_id('su')
target = driver.find_element_by_id('su')
ActionChains(driver).drag_and_drop(element, target).perform()
