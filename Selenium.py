from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# try:
#     open("abc.txt",'r')
#     print(aa)
# except BaseException as msg:
#     print(msg)
driver = webdriver.Chrome()
# driver.get("http:www.126.com")
# driver.find_element_by_id("idInput").clear()
# driver.find_element_by_id("idInput").send_keys("username")
# driver.find_element_by_id("pwdInput").clear()
# driver.find_element_by_id("pwdInput").send_keys("password")
# driver.find_element_by_id("loginBtn").click()
driver.get("http://yunpan.360.cn")
right_click = driver.find_element_by_id("XX")
ActionChains(driver).context_click(right_click).perform()
above = driver.find_element_by_id("id")
ActionChains(driver).move_to_element(above).perform()
double_click = driver.find_element_by_id("XX")
elemrnt = driver.find_element_by_id("xx")
target = driver.find_element_by_id("xx")
ActionChains(driver).drag_and_drop(elemrnt,target).perform()
