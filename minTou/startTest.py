#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing
import unittest


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(MTTestCase('test_case001'))
    # time_str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    # filename = "D:\\appium\\appiumresult\\result_" + time_str + ".html"
    # print (filename)
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #             stream=fp,
    #             title=u'民投金服 APP自动化测试报告 (Android)',
    #             description=u'【测试报告详情】：'
    #             )
    # runner.run(suite)
    # fp.close()
    suite = unittest.defaultTestLoader.discover('.', pattern='test*.py')
    unittest.TextTestRunner().run(suite)


