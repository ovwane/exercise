import re
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'  # 设备版本
desired_caps['deviceName'] = '127.0.0.1:21503'  # 设备名称
# desired_caps['app'] = 'C:\\Users\\SIMO\\Desktop\\weixin_1220.apk'  # 待测应用
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.app.WeChatSplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(10)
driver.find_element_by_id('com.tencent.mm:id/czy').click()
driver.find_element_by_id('com.tencent.mm:id/bw6').click()
_list = driver.find_elements_by_id('com.tencent.mm:id/hk')
_list[0].send_keys('735938470')
_list[1].send_keys('lt19910301.')
driver.find_element_by_id('com.tencent.mm:id/bw7').click()
WebDriverWait(driver, 2002).until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/oc')))
driver.find_element_by_id('com.tencent.mm:id/oc').click()
time.sleep(10)
while True:
    time.sleep(2)
    b = re.findall('(?<=text=")\[微信红包\].*?(?=" class=")', driver.page_source)
    print('获取页面')
    for i in b:
        try:
            print(i)
            driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % i).click()
            b = driver.find_elements_by_name('领取红包')
            driver.find_element_by_android_uiautomator('new UiSelector().text("领取红包")').click()
            print(b)
            try:
                driver.find_element_by_class_name('android.widget.Button').click()
            except:
                driver.find_element_by_accessibility_id('返回').click()
                driver.find_element_by_accessibility_id('返回').click()
            print(1)
            WebDriverWait(driver, 20000).until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/bz0')))
            print(2)
            driver.find_element_by_accessibility_id('返回').click()
            print(3)
            driver.find_element_by_accessibility_id('返回').click()
            print('领取红包')
        except Exception as e:
            print(e)
