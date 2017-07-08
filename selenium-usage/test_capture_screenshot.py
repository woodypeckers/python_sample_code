#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import sys, time
import unittest
from selenium import webdriver


class BaiduTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def testPageTitle(self):
        self.browser.get('https://www.baidu.com')
        self.assertTrue('百度'.decode('utf-8') in self.browser.title)
        time.sleep(2)

        self.browser.get_screenshot_as_file(r"C:\cap\baidu_screen.jpg") #raw_string
        # self.browser.save_screenshot() 已经废弃掉了
        # self.browser.get_screenshot_as_png() 获取文件的二进制数据


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(BaiduTestCase))
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not res.wasSuccessful())