#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@功能：
    使用Windows Internet Explorer测试网站
@注意：
    1. IE目录下需要IEDriverServer.exe文件
    2. IE需要取消保护模式，IE 设置 -> 选项 -> 安全 ->
        Internet 本地Intranet 受信任的站点 受限制的站点
        去掉 启用保护模式的勾
"""
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaiduIE(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(
            executable_path=r'C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe')
        # "c:\\program files\\Internet Explorer\\IEDriverServer.exe"
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
        driver.find_element_by_name("wd").send_keys("selenium ide")
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
        #driver.close()

    # def test_xxx(self):
    #     self.assertTrue(True)
    #     print "hello"

if __name__ == "__main__":
    unittest.main()
