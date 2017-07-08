#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import os, sys, time
import unittest
from selenium import webdriver


class BaiduTestCase(unittest.TestCase):

    def setUp(self):
        self.fp = webdriver.FirefoxProfile()
        self.fp.set_preference("browser.download.folderList", 2)
        self.fp.set_preference("browser.download.manager.showWhenStarting", False)
        self.fp.set_preference("browser.download.dir", os.getcwd())
        self.fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "application/octet-stream") #下载文件类型

        self.driver = webdriver.Firefox()

    def tearDown(self):
        #self.driver.quit()
        pass

    # 与本地的百度输入法冲突
    def testPageTitle(self):
        driver = self.driver
        driver.get("http://pypi.python.org/pypi/selenium")
        driver.find_element_by_link_text("selenium-3.0.2.tar.gz").click()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(BaiduTestCase))
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not res.wasSuccessful())