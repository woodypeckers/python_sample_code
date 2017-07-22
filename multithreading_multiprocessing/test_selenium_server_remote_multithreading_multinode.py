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
host_dict = {
             'tt': ["http://192.168.5.148:1234/wd/hub", "chrome"],
             'ljl': ["http://192.168.5.152:5555/wd/hub", 'internet explorer'],
             'lx': ["http://192.168.5.154:2347/wd/hub", 'chrome'],
             'zjw': ["http://192.168.5.180:7777/wd/hub", 'firefox'],
             'ld': ["http://192.168.5.150:1111/wd/hub", 'firefox']
             }

desired_capabilities = {'platform': 'ANY',
                        'browserName': 'firefox',
                        'version': '',
                        'javascriptEnabled': True}


def run_test1(host, desired_capabilities):
    driver = Remote(command_executor=host, desired_capabilities=desired_capabilities)
    driver.get('http://%s/bugfree' % IP)
    time.sleep(2)
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

def run_test2(host, desired_capabilities):
    driver = Remote(command_executor=host, desired_capabilities=desired_capabilities)
    driver.get('https://www.baidu.com')
    time.sleep(2)
    driver.find_element_by_id("kw").send_keys("remote")
    driver.find_element_by_id("su").click()
    time.sleep(2)
    driver.quit()

def run_all(host, desired_capabilities):
    run_test1(host, desired_capabilities)
    run_test2(host, desired_capabilities)

def main():
    threads = []
    for i in host_dict.keys():
        try:
            host, browser = host_dict[i]
            print host, browser
            dc = desired_capabilities.copy()
            dc['browserName'] = browser
            if i in ['tt', 'ljl', 'zjw']:
                threads.append(threading.Thread(target=run_test1,
                                                name=dc['browserName'],
                                                args=(host, dc)))
            else:
                threads.append(threading.Thread(target=run_test2,
                                                name=dc['browserName'],
                                                args=(host, dc)))
        except Exception:
            print Exception.message
    for t in threads:
        print t
        t.start()

    for t in threads:
        t.join()
    print "All done"


if __name__ == "__main__":
    main()
