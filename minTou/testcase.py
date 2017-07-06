#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

import unittest
from appium import webdriver
import os
import time
import user

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'Samsung Galaxy S7'
desired_caps['appPackage'] = 'com.mintou.finance'
desired_caps['appActivity'] = '.ui.LaucherTaskActivity'
desired_caps['appWaitActivity'] = '.ui.MainActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.deactivate_ime_engine()


class MTTestCase(unittest.TestCase):

    def setUp(self):
        print(u"开始测试时间:" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    def tearDown(self):
        # driver.quit()
        try:
            driver.get_screenshot_as_file(
                'G:\\appium\\screenshots\\' + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.png')
        except IOError:
            print(u'截图失败')
        print(u"完成测试时间:" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    # 注册
    def test_case001(self):
        driver.implicitly_wait(10)
        driver.find_element_by_name("资产").click()
        driver.find_element_by_name("注册送999元").click()
        user.User(driver).test_register()

    # 注册成功后设置交易密码
    def test_case002(self):
        driver.find_element_by_name("认证银行卡").click()
        user.User(driver).test_trans_pass()

    # 认证
    def test_case003(self):
        user.User(driver).test_quick_pay("交通银行")

