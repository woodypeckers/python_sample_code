#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver import Remote


class TestMultipleEnv(unittest.TestCase):
    def setUp(self):
        self.available_node = {
            'hub': ('http://127.0.0.1:4444/wd/hub', 'firefox'),
            #'node1': ('http://127.0.0.1:5555/wd/hub', 'chrome'),
            #'node2': ('http://127.0.0.1:6666/wd/hub', 'internet explorer'),
            # 'zhanglei': ('http://192.168.2.7:6666/wd/hub', 'chrome'),
            # 'zhanyong': ('http://192.168.2.11:9999/wd/hub', 'chrome'),
            # 'huangquan': ('http://192.168.2.28:7777/wd/hub', 'chrome'),
            # 'jaydan': ('http://192.168.2.13:5555/wd/hub', 'chrome')
            # 'jiale': ('http://192.168.2.16:5555/wd/hub', 'chrome'),
            'wangming': ('http://172.21.20.2:5555/wd/hub', 'chrome')
        }
        self.driver = None
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        pass

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

    def test_nodes_open_and_search(self):
        for node in self.available_node.keys():
            if node == 'hub':
                continue
            self.driver = Remote(self.available_node[node][0],
                                 desired_capabilities={'platform': 'ANY',
                                                       'browserName': self.available_node[node][1],
                                                       'version': '',
                                                       'javascriptEnabled': True})
            self.driver.implicitly_wait(30)
            driver = self.driver
            driver.get(self.base_url)
            driver.find_element_by_id("kw").send_keys("remote")
            driver.find_element_by_id("su").click()
            # if self.driver is not None:
            #     self.driver.quit()

if __name__ == "__main__":
    unittest.main()
