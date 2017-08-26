#encoding:utf-8
import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class QXueYou(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'H6D5T15606000272'
        # desired_caps['app'] = PATH(
        #     '../../../sample-code/apps/ContactManager/ContactManager.apk'
        # )
        desired_caps['appPackage'] = 'com.iqtogether.qxueyou'
        desired_caps['appActivity'] = 'com.iqtogether.qxueyou.activity.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # def tearDown(self):
    #     self.driver.quit()

    def test_weixin_login(self):
        sleep(3)
        print self.driver.page_source
        btns = self.driver.find_elements_by_class_name("android.widget.Button")
        btns[2].click()

        sleep(2)
        wxBtn = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '微信登录')]")
        wxBtn.click()
        sleep(5)
        print self.driver.page_source
        # login = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView")')
        # login.click()
        wxlogin = self.driver.find_element_by_class_name("android.widget.TextView")
        print wxlogin
        wxlogin.click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(QXueYou)
    unittest.TextTestRunner(verbosity=2).run(suite)
