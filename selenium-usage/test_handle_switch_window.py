#!/usr/bin/env python
#encoding:utf-8
__author__ = 'Samren'
import os, sys, time
import unittest
from selenium import webdriver


class BaiduSearchTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"

    #def tearDown(self):
    #    self.driver.quit()

    def test_handle_windows(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys(u"samren博客园")
        driver.find_element_by_id("su").click()

        driver.find_element_by_partial_link_text(u"GitHub命令精简教程").click()
        win_list = driver.window_handles
        print driver.window_handles
        print driver.current_window_handle
        print driver.current_url
        driver.switch_to.window(win_list[1])
        print driver.current_window_handle
        print driver.current_url


if __name__ == '__main__':
    unittest.main()