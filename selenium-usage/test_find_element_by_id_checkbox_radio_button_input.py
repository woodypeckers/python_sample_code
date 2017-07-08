# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time, re


class BugfreeLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30) #智能等待
        self.base_url = "http://localhost"
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        print '当前的url是：', driver.current_url
        print '标题是：', driver.title
        print '当前窗口大小：', driver.get_window_size()
        driver.maximize_window()
        self.assertEqual(u"登录 - BugFree", driver.title)
        driver.find_element_by_id("LoginForm_username").click()
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("LoginForm_language").click()
        Select(driver.find_element_by_id("LoginForm_language")).select_by_value("en")
        Select(driver.find_element_by_id("LoginForm_language")).select_by_value("zh_cn")
        if not driver.find_element_by_id("LoginForm_rememberMe").is_selected():
            driver.find_element_by_id("LoginForm_rememberMe").click()
        if driver.find_element_by_id("LoginForm_rememberMe").is_selected():
            driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()

        self.assertRegexpMatches(driver.page_source, r"<title>BugFree</title>")
        #self.assertEqual(u'BugFree', driver.title)

    def test_bugfree_click_one_case(self):
        driver = self.driver
        # link=Sample：欢迎使用BugFree！
        driver.get(self.base_url + "/bugfree/index.php/bug/1")
        driver.find_element_by_name("yt2").click()
        driver.find_element_by_name("yt0").click()
        driver.get("http://www.baidu.com")
        driver.back()

    def test_xxx(self):
        print "hello world"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
