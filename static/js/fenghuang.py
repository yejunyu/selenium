#!/usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'Ye Jun yu'
# email: yyyejunyu@gmail.com
# date:{17-7-27}

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


headers = {
    "Referer": "http://yejunyu.com",
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
}
desire = webdriver.DesiredCapabilities.CHROME.copy()
desire.setdefault("headers",headers)
print (desire)
for key, value in headers.items():
    webdriver.DesiredCapabilities.CHROME['chrome.page.customHeaders.{}'.format(key)] = value
driver = webdriver.Chrome(desired_capabilities=desire)
url = 'https://www.ifeng.com'
driver.get(url)
print (driver.get_cookies())
# print (driver.page_source)
time.sleep(1)
# js = 'window.open("{}");'.format(url)
# driver.execute_script(js)
# driver.find_element_by_css_selector("body").send_keys(Keys.CONTROL+"t")
# handles = driver.window_handles
# driver.switch_to.window(handles[-1])
# time.sleep(20)
driver.close()
driver.quit()