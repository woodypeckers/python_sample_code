#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#done : 执行chrome 、ie都有问题，应该是driver没设置好
#解决把chromedriver.exe放到 C:\Python27\Scripts 里
class TestChrome(unittest.TestCase):
    def setUp(self):
        self.capabilities = {}
        self.command_executor = "http://192.168.2.17:4444/wd/hub"
        #self.command_executor = "http://192.168.5.140:4444/wd/hub"
        self.capabilities = DesiredCapabilities.CHROME.copy()
        self.capabilities['browserName'] = 'chrome'
        self.capabilities['platform'] = "WINDOWS"
        self.capabilities['version'] = "7"
        self.base_url = "https://www.baidu.com"
        self.driver = Remote(command_executor=self.command_executor,
                             desired_capabilities=self.capabilities)

        self.driver.implicitly_wait(30)

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("test chrome")
        driver.find_element_by_id("su").click()
        driver.get_screenshot_as_file("./chrome_capture.jpg")

if __name__ == "__main__":
    unittest.main()
