*** Settings ***
Library           Selenium2Library
Library           string
Library           requests

*** Test Cases ***
测试用例1
    open browser    http://www.baidu.com    ie
    page should contain    百度一下
    log    已经打开ie
    capture page screenshot    selenium-screenshot-01.png
    delete all cookies
    close browser
