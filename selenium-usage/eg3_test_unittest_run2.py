#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import sys
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
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(BaiduTestCase))
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not res.wasSuccessful())