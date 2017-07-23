*** Settings ***
Library           Selenium2Library
Resource          resources.robot

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

登录成功_admin
    [Template]    登录验证通用逻辑
    admin    123456    退出
    [Teardown]

登录失败_无效的用户名
    [Template]    登录验证通用逻辑
    invalid    123456    用户名不存在
    [Teardown]

登录失败_admin错误密码
    [Template]    登录验证通用逻辑
    admin    invalid    用户名和密码不匹配
    [Teardown]

*** Keywords ***
登录验证通用逻辑
    [Arguments]    ${username}    ${password}    ${verify_flag}
    log many    ${username}    ${password}    ${verify_flag}
    打开登录页面
    输入用户名    ${username}
    输入密码    ${password}
    点击登录按钮
    页面应该包含    ${verify_flag}
    [Teardown]    close browser
