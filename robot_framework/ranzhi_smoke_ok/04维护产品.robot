*** Settings ***
Resource          业务关键字.robot

*** Test Cases ***
新增机器人产品线
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[7]/a
    Click Element    xpath=html/body/div[2]/div[2]/div[1]/div[2]/a
    Sleep    1s
    Input Text    xpath=//*[@id='values[]']    机器人
    Click Element    xpath=//*[@id='submit']

新增机器人产品
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[7]/a
    Click Element    xpath=//*[@id='menuActions']/a
    Sleep    1s
    Input Text    xpath=//*[@id='name']    扫地机器人
    Input Text    xpath=//*[@id='code']    sz001
    Select From List By Index    xpath=//*[@id='status']    1
    Click Element    xpath=//*[@id='submit']

删除机器人产品
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[7]/a
    Click Element    xpath=//*[@id='productList']/tbody/tr/td[8]/a[2]
    Dismiss Alert
