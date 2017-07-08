# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner

class Baidu_Firefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"

    def tearDown(self):
        self.driver.quit()

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        input = driver.find_element_by_id("kw")
        input.click()
        input.clear()
        input.send_keys("selenium ide")
        time.sleep(2)
        input.send_keys(Keys.BACK_SPACE * 4)
        time.sleep(2)
        input.send_keys(Keys.SPACE)
        time.sleep(1)
        input.send_keys(u"知识改变命运")
        #driver.find_element_by_id("su").click()
        driver.find_element_by_css_selector("#su").click()
        time.sleep(3)

    # def test_compose_email(self):
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     time.sleep(2)
    #     self.assertTrue(True)
    #
    # def test_delete_email(self):
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     time.sleep(2)
    #     self.assertNotEqual("aa", 'aa')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(Baidu_Firefox))

    fp = open('./test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'百度搜索测试报告',
                            description=u"测试用例执行情况：")
    runner.run(suite)
    fp.close()
