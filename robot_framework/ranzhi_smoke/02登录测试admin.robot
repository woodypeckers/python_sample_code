*** Settings ***
Library           Selenium2Library
Resource          公共关键字.robot

*** Test Cases ***
管理员登录
    打开浏览器并转到登录页面
    Input Text    xpath=.//*[@id='account' and @name='account']    嘎嘎嘎
