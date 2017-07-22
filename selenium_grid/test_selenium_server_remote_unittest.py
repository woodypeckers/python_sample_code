#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver import Remote


class Firefox(unittest.TestCase):
    def setUpClass(cls):
        pass

    def tearDownClass(cls):
        pass

    def setUp(self):
        command_executor = 'http://127.0.0.1:4444/wd/hub'
        desired_capabilities = {'platform': 'ANY',
                                'browserName': 'firefox',
                                'version': '',
                                'javascriptEnabled': True}
        self.driver = Remote(command_executor, desired_capabilities)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("remote")
        driver.find_element_by_id("su").click()

if __name__ == "__main__":
    unittest.main()
