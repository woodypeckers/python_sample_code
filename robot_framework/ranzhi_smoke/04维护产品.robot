*** Settings ***
Library           Selenium2Library
Resource          业务关键字.robot
Resource          公共关键字.robot

*** Test Cases ***
TC01_新建产品
    管理员登陆成功    admin    admin8888    退出
    Click Button    xpath=//*[@id="s-menu-1"]/button
    Sleep    2s
    Select Frame    id=iframe-1    #选择iframe
    Click Link    产品
    Click Element    xpath=//*[@id="menuActions"]/a    #点击新建产品
    Sleep    2s
    Input Text    id=name    测试
