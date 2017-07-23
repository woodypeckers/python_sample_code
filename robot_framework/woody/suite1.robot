*** Settings ***
Library           Selenium2Library

*** Test Cases ***
case1
    log    啄木鸟
    Open Browser    http://localhost/bugfree    ie    ie
    Capture Page Screenshot
    Open Browser    http://www.baidu.com    chrome    chrome
    Switch Browser    ie
    Input Text    id=LoginForm_username    admin
    Input Password    id=LoginForm_password    123456
    Capture Page Screenshot
    close all browsers
