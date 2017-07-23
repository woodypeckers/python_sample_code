*** Settings ***
Library           Selenium2Library

*** Test Cases ***
iframe_demo
    open browser    http://localhost/bugfree    chrome
    Select frame    id=fra
    unselect frame
    log source
    close browser

window_demo
    open browser    http://localhost/bugfree
    click button    id=10
    confirm action
    Select Window
    log source
    close browser

switch_browser
    open browser    http://localhost/bugfree    ie    ie
    ${title1}    Get Title
    open browser    http://www.baidu.com    chrome    chrome
    ${title2}    GetTitle
    Switch Browser    ie
    log    切换到ie
    close all browsers
