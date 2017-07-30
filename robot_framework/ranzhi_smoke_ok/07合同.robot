*** Settings ***
Resource          公共关键字.robot
Resource          业务关键字.robot
Library           Selenium2Library

*** Test Cases ***
创建合同
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[3]/a    #导航栏，合同
    Click Element    xpath=//*[@id='menuActions']/a    #创建合同
    Sleep    1s
    Click Element    xpath=//*[@id='customer_chosen']/a
    Click Element    xpath=//*[@id='customer_chosen']/div/ul/li[1]
    Input Text    xpath=//*[@id='name']    张三的合同
    Select Frame    xpath=//*[@id='ajaxForm']/table/tbody/tr[12]/td/div/div[2]/iframe
    Input Text    xpath=html/body    hahaha
    Unselect Frame
    Select Frame    id=iframe-1
    Click Element    xpath=//*[@id='submit']

删除合同
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[3]/a
    Click Element    xpath=//*[@id='contractList']/tbody/tr/td[11]/div/a
    Sleep    1s
    Click Element    xpath=//*[@id='contractList']/tbody/tr/td[11]/div/ul/li[2]/a
    Dismiss Alert
