*** Settings ***
Resource          公共关键字.robot
Resource          业务关键字.robot
Library           Selenium2Library

*** Test Cases ***
创建订单
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[2]/a
    Click Element    xpath=//*[@id='menuActions']/a    #创建订单的按钮
    Sleep    2s
    Click Element    xpath=//*[@id='customer_chosen']/a
    Click Element    xpath=//*[@id='customer_chosen']/div/ul/li[1]
    Click Element    xpath=//*[@id='product_chosen']/ul
    Click Element    xpath=//*[@id='product_chosen']/div/ul/li
    Input Text    xpath=//*[@id='plan']    1234567890
    Click Element    xpath=//*[@id='submit']

删除订单
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[2]/a
    Sleep    1s
    Click Element    xpath=html/body/div[2]/div[2]/table/tbody/tr/td[11]/div/a
    Sleep    1s
    Click Element    xpath=html/body/div[2]/div[2]/table/tbody/tr/td[11]/div/ul/li[4]/a
    Dismiss Alert
