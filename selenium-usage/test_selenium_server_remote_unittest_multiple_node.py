#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestMultipleEnv(unittest.TestCase):
    def setUp(self):
        self.available_node = {
            'node1': ('http://127.0.0.1:5555/wd/hub', 'chrome'),
            'wuxing': ('http://192.168.6.204:6666/wd/hub', 'firefox'),
            'juwei': ('http://192.168.6.184:9546/wd/hub', 'chrome'),
            'zhiping': ('http://192.168.6.185:7777/wd/hub', 'firefox'),
            'jiangling': ('http://192.168.7.8:9546/wd/hub', 'internet explorer'),
            'zhijie': ('http://192.168.6.17:7890/wd/hub', 'chrome'),
            'junjie': ('http://192.168.6.208:9546/wd/hub', 'internet explorer')
        }
        self.driver = None
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

    def test_wuxing_open_and_search(self):
        self.driver = Remote(self.available_node['wuxing'][0],
                             desired_capabilities={'platform': 'ANY',
                                                   'browserName': self.available_node['wuxing'][1],
                                                   'version': '',
                                                   'javascriptEnabled': True})
        self.driver.implicitly_wait(30)
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("remote")
        driver.find_element_by_id("su").click()

    def test_node1_open_and_search(self):
        self.driver = Remote(self.available_node['node1'][0],
                             desired_capabilities={'platform': 'ANY',
                                                   'browserName': self.available_node['node1'][1],
                                                   'version': '',
                                                   'javascriptEnabled': True})
        self.driver.implicitly_wait(30)
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("remote")
        driver.find_element_by_id("su").click()

if __name__ == "__main__":
    unittest.main()
