*** Settings ***
Library           Selenium2Library

*** Test Cases ***
baidu_suite
    open Browser    http://www.baidu.com
    input text    id=kw    hello
    click button    id=su
