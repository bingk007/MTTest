#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

import random
import unittest
import os
from appium import webdriver
import time
import db
import common
import gVariable
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class User:
    def __init__(self, driver):
        self.driver = driver

    def test_register(self):
        self.driver.find_element_by_name("请输入常用手机号码").send_keys(gVariable.GVariable.teleNum)
        print(gVariable.GVariable.teleNum)
        self.driver.find_element_by_name("下一步").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("确定").click()
        self.driver.implicitly_wait(10)
        views = self.driver.find_elements_by_class_name('android.widget.EditText')
        views[0].send_keys(db.DB().get_code())
        views[1].send_keys('aaa12345')
        views[2].send_keys('13728728079')
        self.driver.hide_keyboard()
        self.driver.find_element_by_name("完成注册  速领福利").click()
        WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located((By.NAME, '注册成功，获得999元优惠券')))

    def test_trans_pass(self):
        WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located((By.NAME, '设置交易密码')))
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys('a1234567')
        self.driver.find_element_by_name('确定').click()

    def test_quick_pay(self, bank):
        self.driver.activate_ime_engine("io.appium.android.ime/.UnicodeIME")
        # print(self.driver.active_ime_engine)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("请输入您的真实姓名").send_keys(u"民投君")
        self.driver.deactivate_ime_engine()
        self.driver.find_element_by_name("请输入您的身份证号").send_keys(gVariable.GVariable().make_id())
        self.driver.find_element_by_name("请输入您的银行卡号").send_keys(gVariable.GVariable().make_card(bank))
        self.driver.hide_keyboard()
        self.driver.find_element_by_name('下一步').click()
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys(db.DB().get_code())
        self.driver.find_element_by_name('确定认证').click()
        WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located((By.NAME, '您的银行卡已成功认证绑定')))



















