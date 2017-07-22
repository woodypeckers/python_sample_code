#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver import Remote
"""
注意：需要安装Safari浏览器
"""

class TestSafari(unittest.TestCase):
    def setUp(self):
        self.dc = {'browserName': 'safari'}
        self.command_executor = "http://127.0.0.1:4444/wd/hub"
        self.driver = None
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

    def test_open_and_search(self):
        self.driver = Remote(self.command_executor,
                             desired_capabilities=self.dc)
        self.driver.implicitly_wait(30)
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("remote")
        driver.find_element_by_id("su").click()

if __name__ == "__main__":
    unittest.main()
