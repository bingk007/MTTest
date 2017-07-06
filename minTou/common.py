#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing

from appium.webdriver.common.touch_action import TouchAction


class Common:
    def __init__(self, driver):
        self.driver = driver

    def recover(self):

        while True:
            try:
                if self.driver.find_element_by_name('首页'):
                    break
            except:
                self.driver.keyevent(4)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipe_left(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_up(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    def gesture(self):
        el = self.driver.find_elements_by_class_name('android.view.View')
        TouchAction(self.driver).press(el[0]).move_to(el[1]).move_to(el[4]).move_to(el[7]).move_to(
            el[8]).release().perform()


