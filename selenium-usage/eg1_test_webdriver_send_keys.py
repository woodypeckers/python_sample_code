#!/usr/bin/env python
#encoding:utf-8
"""

"""
__author__ = 'Samren'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_firefox():
    browser = webdriver.Firefox()

    browser.get('http://www.yahoo.com')
    print browser.title
    assert 'Yahoo' in browser.title

    elem = browser.find_element_by_name('p')  # Find the search box
    elem.send_keys('seleniumhq' + Keys.RETURN)

    browser.quit()


if __name__ == '__main__':
    test_firefox()