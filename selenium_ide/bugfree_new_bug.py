# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BugfreeNewBug(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bugfree_new_bug(self):
        driver = self.driver
        driver.find_element_by_link_text(u"新建 Bug").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | 新建Bug | ]]
        driver.find_element_by_id("BugInfoView_title").clear()
        driver.find_element_by_id("BugInfoView_title").send_keys("autotest002")
        driver.find_element_by_id("BugInfoView_assign_to_name").click()
        driver.find_element_by_css_selector("li.ac_even").click()
        driver.find_element_by_id("BugInfoView_mail_to").click()
        driver.find_element_by_xpath("//div[5]/ul/li").click()
        Select(driver.find_element_by_id("BugInfoView_severity")).select_by_visible_text("1")
        Select(driver.find_element_by_id("Custom_BugType")).select_by_visible_text(u"代码错误")
        Select(driver.find_element_by_id("Custom_HowFound")).select_by_visible_text(u"单元测试")
        driver.find_element_by_id("Custom_OpenedBuild").clear()
        driver.find_element_by_id("Custom_OpenedBuild").send_keys("001")
        driver.find_element_by_name("yt0").click()
        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
