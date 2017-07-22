#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver import Remote


class TestMultipleEnv(unittest.TestCase):
    def setUp(self):
        self.available_node = {
            'hub': ('http://127.0.0.1:4444/wd/hub', 'firefox'),
            'node1': ('http://127.0.0.1:5555/wd/hub', 'chrome')
        }
        self.driver = None
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

    # def test_hub_open_and_search(self):
    #     self.driver = Remote(self.available_node['hub'][0],
    #                          desired_capabilities
    #                          = {'platform': 'ANY',
    #                             'browserName': self.available_node['hub'][1],
    #                             'version': '',
    #                             'javascriptEnabled': True
    #                          })
    #     self.driver.implicitly_wait(30)
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.find_element_by_id("kw").send_keys("remote")
    #     driver.find_element_by_id("su").click()

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
