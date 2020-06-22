#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
#@author:SSR
#@file: Test002.py 
#@time: 2020/06/21
#@software: PyCharm

from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://cloud.tencent.com/")
driver.maximize_window()
assert  "腾讯云" in driver.title
print(driver.title)
ele = driver.find_element_by_xpath("//span[@class='J-placeholderSearchWord']")
ele.click()
ele =  driver.find_element_by_xpath("//div[@id='navigationBar']//input[@class='search-ipt J-qcIptSearch']")
ele.clear()
ele.send_keys("python")
ele.send_keys(Keys.RETURN)
assert "No result found. " not in driver.page_source
driver.close()
