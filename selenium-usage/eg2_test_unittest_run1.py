#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
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


if __name__ == '__main__':
    unittest.main(verbosity=2)
