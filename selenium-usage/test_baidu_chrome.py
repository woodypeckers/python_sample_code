#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@功能：
    使用Windows Chrome测试Web
@注意：
    1. Chrome.exe目录下需要 chromedriver.exe 文件
"""
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaiduChrome(unittest.TestCase):
    def setUp(self):
        self.executable_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        #self.driver = webdriver.Chrome(executable_path=self.executable_path)
        #有 --ignore-certificate-errors错误提示
        #self.driver = webdriver.Chrome(executable_path=self.executable_path)

        # 参考链接：http://blog.csdn.net/xiecj_2006/article/details/43086731
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('test-type')
        self.driver = webdriver.Chrome(executable_path=self.executable_path, chrome_options=self.option)
        #self.driver = webdriver.Chrome(executable_path=self.executable_path)
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
        time.sleep(5)
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
    #     print "hello"

if __name__ == "__main__":
    unittest.main()
