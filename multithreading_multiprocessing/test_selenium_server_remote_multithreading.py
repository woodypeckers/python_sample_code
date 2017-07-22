#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
说明：需要运行命令 java -jar selenium-server-standalone-2.53.0.jar
注意：
1. 不能添加-role hub参数
2. 深拷贝和浅拷贝
"""
from selenium.webdriver import Remote
import sys, time, traceback
import threading


IP = '192.168.5.140'
#IP = '192.168.1.16'
host_dict = {'rs_ff': ["http://%s:5555/wd/hub" % IP, "firefox"],
             'rs_ie': ["http://%s:6666/wd/hub" % IP, 'internet explorer'],
             'rs_chrome': ["http://%s:6666/wd/hub" % IP, 'chrome']
             }

desired_capabilities = {'platform': 'ANY',
                        'browserName': 'firefox',
                        'version': '',
                        'javascriptEnabled': True}


def run_browser(host, desired_capabilities):
    driver = Remote(command_executor=host, desired_capabilities=desired_capabilities)
    driver.get('http://%s/bugfree' % IP)
    time.sleep(2)
    # driver.get('https://www.baidu.com')
    # driver.find_element_by_id("kw").send_keys("remote")
    # driver.find_element_by_id("su").click()
    driver.find_element_by_id("LoginForm_username").click()
    driver.find_element_by_id("LoginForm_username").clear()
    driver.find_element_by_id("LoginForm_username").send_keys("admin")
    time.sleep(2)
    driver.find_element_by_id("LoginForm_password").clear()
    driver.find_element_by_id("LoginForm_password").send_keys("123456")
    time.sleep(2)
    driver.find_element_by_id("SubmitLoginBTN").click()
    time.sleep(2)
    driver.quit()


def main():
    threads = []
    for i in host_dict.keys():
        host, browser = host_dict[i]
        print host, browser
        dc = desired_capabilities.copy()
        dc['browserName'] = browser
        threads.append(threading.Thread(target=run_browser,
                                        name=dc['browserName'],
                                        args=(host, dc)))
    for t in threads:
        print t
        t.start()

    for t in threads:
        t.join()
    print "All done"


if __name__ == "__main__":
    main()
