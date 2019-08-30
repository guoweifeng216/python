from selenium import webdriver
from time import sleep

first = "http:www.baidu.com"

driver = webdriver.Chrome()
driver.get(first)
# driver.set_window_size(600, 800)
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# second = "http:news.baidu.com"
# driver.get(second)
# driver.back()
# driver.refresh()
# sleep(2)
# driver.get_screenshot_as_file("D:\\wfguo\\baidu_img.jpg")
# 获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)
# 返回百度页面底部的备案信息
text = driver.find_element_by_id('cp').text
print(text)
# 返回元素的属性
attribure = driver.find_element_by_id('kw').get_attribute('type')
print(attribure)
# 返回元素的结果是否可见，结果为T or F
result = driver.find_element_by_id('kw').is_displayed()
print(result)
# driver.quit()
