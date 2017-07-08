#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
说明：需要运行命令 java -jar selenium-server-standalone-2.53.0.jar
注意，不能添加-role hub参数
"""
from selenium.webdriver import Remote
import sys, time, traceback

if __name__ == "__main__":
    # command_executor = 'http://127.0.0.1:4444/wd/hub'
    host_dict = {'rs_pc': ["http://192.168.5.140:5555/wd/hub", "internet explorer"],
                 'tny_pc': ["http://192.168.5.148:1234/wd/hub", 'internet explorer'],
                 "ljl_pc": ["http://192.168.5.152:2222/wd/hub", "internet explorer"],
                 'lidan_pc': ["http://192.168.5.150:1111/wd/hub", "internet explorer"],
                 "lixiao_pc": ["http://192.168.5.154:6666/wd/hub", "internet explorer"],
                 "jiaowei_pc": ["http://192.168.5.180:7777/wd/hub", "internet explorer"]
                 }
    desired_capabilities = {'platform': 'ANY',
                            'browserName': 'firefox',
                            'version': '',
                            'javascriptEnabled': True}
    for i in host_dict.keys():
        try:
            host, browser = host_dict[i]
            print i, host, browser
            desired_capabilities['browserName'] = 'internet explorer'
            driver = Remote(command_executor=host, desired_capabilities=desired_capabilities)
            driver.get('http://192.168.5.140/bugfree')
            time.sleep(2)
            #driver.get('http://www.baidu.com')
            #driver.find_element_by_id("kw").send_keys("remote")
            #driver.find_element_by_id("su").click()
            driver.quit()
        except Exception:
            print traceback.print_exc(file=sys.stdout)
