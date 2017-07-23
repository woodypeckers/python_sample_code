*** Settings ***
Suite Teardown    Close All Browsers
Test Teardown
Test Template     公共登录逻辑
Library           Selenium2Library
Resource          resources.robot

*** Test Cases ***
管理员用户_登录成功
    admin    123456    退出

管理员用户_登录失败_错误的用户名
    invalid    123456    用户名不存在

管理员用户_登录失败_错误的密码
    admin    invalid    用户名和密码不匹配

*** Keywords ***
公共登录逻辑
    [Arguments]    ${username}    ${password}    ${keyword}
    打开登录页面
    输入用户名    ${username}
    输入密码    ${password}
    点击登录按钮
    页面应该包含    ${keyword}
