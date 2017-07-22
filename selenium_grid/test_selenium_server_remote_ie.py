#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#done : 执行chrome 、ie都有问题，应该是driver没设置好
#解决把IEDriverServer.exe放到 C:\Python27\Scripts 里
class TestIE(unittest.TestCase):
    def setUp(self):
        self.capabilities = {}
        self.command_executor = "http://192.168.6.23:5555/wd/hub"
        self.capabilities['browserName'] = 'internet explorer'
        self.capabilities['platform'] = "WINDOWS"
        self.capabilities['version'] = "7"
        self.driver = None
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

    def test_open_and_search(self):
        self.driver = Remote(self.command_executor,
                             desired_capabilities=self.capabilities)
        self.driver.implicitly_wait(30)
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("test ie")
        driver.find_element_by_id("su").click()
        #driver.get_screenshot_as_file("./ie_capture.jpg")

if __name__ == "__main__":
    unittest.main()
