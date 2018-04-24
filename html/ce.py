import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(5)
for i in [1,2,3]:
    driver.find_element_by_id('kw').send_keys((Keys.CONTROL+'t'))
