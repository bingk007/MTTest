#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

class Account:

    def __init__(self, driver):
        self.driver = driver

    def recharge(self,money):
        self.driver.find_element_by_name("充值金额100元起，0元手续费").send_keys(money)
        self.driver.hide_keyboard()
        self.driver.find_element_by_name('下一步').click()