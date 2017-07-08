#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


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

        # 移动鼠标到“设置”上面
        link = driver.find_element_by_link_text(u"设置")
        ActionChains(driver).move_to_element(link).perform()
        # ActionChains(driver).double_click(link).perform()  双击操作
        # ActionChains(driver).drag_and_drop(element, target).perform()  鼠标拖放操作
        time.sleep(3)

        # 点击 “搜索设置”
        driver.find_element_by_class_name("setpref").click()
        #driver.find_element_by_link_text(u"搜索设置").click()
        time.sleep(3)

        # 保存设置
        driver.find_element_by_class_name("prefpanelgo").click()
        time.sleep(3)

        # 接受弹框
        #driver.switch_to_alert().accept()  #已废弃的用法
        print driver.switch_to.alert.text
        driver.switch_to.alert.accept()  # 点击确定
        time.sleep(3)
        

if __name__ == "__main__":
    unittest.main()
