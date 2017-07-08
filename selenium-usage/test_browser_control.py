#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Firefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(5)
        print driver.get_window_size()
        driver.maximize_window()
        second_url = 'http://news.baidu.com'
        print "now access %s" % second_url
        driver.get(second_url)

        # back to index.html
        print "back to %s" % self.base_url
        driver.back()
        time.sleep(3)

        # forword to news page
        print "forword to %s" % second_url
        driver.forward()
        time.sleep(3)

        # refresh page
        print "refresh page"
        driver.refresh()
        time.sleep(3)



if __name__ == "__main__":
    unittest.main()
