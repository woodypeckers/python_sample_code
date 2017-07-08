#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaiduFirefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(10)
        driver.find_element_by_name("wd").clear()
        driver.find_element_by_name("wd").send_keys(u"samren 博客")
        time.sleep(3)
        driver.find_element_by_name("wd").send_keys(Keys.SPACE)
        time.sleep(2)
        #英文例子
        #driver.find_element_by_name("wd").send_keys("xy")
        #中文例子，注意：中文字符串前必须加u，表示unicode字符串
        driver.find_element_by_name("wd").send_keys(u"教程")

        time.sleep(2)
        driver.find_element_by_name("wd").send_keys(Keys.BACK_SPACE * 2)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        # ERROR: Caught exception [ERROR: Unsupported command [openWindow | http://news.baidu.com/ | ]]
        driver.close()

    # def test_xxx(self):
    #     self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
