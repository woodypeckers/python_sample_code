#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestFirefox(unittest.TestCase):
    def setUp(self):
        self.command_executor = "http://192.168.6.23:5555/wd/hub"
        self.capabilities = DesiredCapabilities.FIREFOX.copy()
        self.capabilities['platform'] = "WINDOWS"
        self.capabilities['version'] = "7"
        self.base_url = "https://www.baidu.com"
        self.driver = Remote(self.command_executor,
                             desired_capabilities=self.capabilities)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("test firefox")
        driver.find_element_by_id("su").click()
        driver.get_screenshot_as_file("./remote_firefox_capture.jpg")

if __name__ == "__main__":
    unittest.main()
