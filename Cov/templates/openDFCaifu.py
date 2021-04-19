# -*- coding:utf-8 -*-
import pymysql
import time
import json
import traceback
import requests
from selenium.webdriver import Chrome,ChromeOptions

option = ChromeOptions()
option.add_argument("--headless")  # 隐藏浏览器
option.add_argument("--no-sandbox")  # linux下启动沙盘模式
browser = Chrome(options=option)
# browser = Chrome()
url = "http://quote.eastmoney.com/stock_list.html"
browser.get(url)
# time.sleep(1)   #等待1秒
browser.find_element_
c = browser.find_element_by_xpath('//*[@id="1"]/h3/a')
href = c.get_attribute('href')
browser.get(href)
# print(browser.current_window_handle)
print dir(browser)
print(browser.current_url)



