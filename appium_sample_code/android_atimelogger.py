import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = 'emulator-5554'
        # desired_caps['app'] = PATH(
        #     '../../../sample-code/apps/ContactManager/ContactManager.apk'
        # )
        desired_caps['appPackage'] = 'com.aloggers.atimeloggerapp'
        desired_caps['appActivity'] = '.ui.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # def tearDown(self):
    #     self.driver.quit()

    def test_add_contacts(self):
        imageviews = self.driver.find_elements_by_class_name("android.widget.ImageView")
        imageviews[0].click()
        #问题 uiautomator无法获取动态元素的xml



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
