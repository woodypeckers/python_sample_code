#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import os, sys, time
import unittest
from selenium import webdriver


class BaiduTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # 向cookie中添加信息
        self.driver.add_cookie({'name': 'key-value_sam', 'value':'vale-bbbb'})
        self.driver.add_cookie({"name": "samren", "value": "is a good man"})

    #def tearDown(self):
    #    self.driver.quit()

    def test_get_cookies(self):
        driver = self.driver
        for item in driver.get_cookies():
            print "%s 's value is: %s" % (item['name'], item['value'])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(BaiduTestCase))
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not res.wasSuccessful())