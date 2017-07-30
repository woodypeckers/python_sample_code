*** Settings ***
Library           Selenium2Library
Resource          resources_ranzhi.robot

*** Test Cases ***
验证登录成功1
    [Template]    open browser and login1
    admin    admin8888

正常登录退出
    open browser and login
    logout and close browser

正常跳转日常办公模块
    [Setup]    open browser and login
    sleep3s
    jump OA
    sleep3s
    [Teardown]    logout and close browser

日常办公_新增项目
    [Setup]    open browser and login
    jump OA
    Select Frame    id = iframe-2
    跳转oa项目页面
    input_project_information
    sleep    1s
    Unselect Frame
    ${title}=    Get Title
    Should Contain    ${title}    然之协同
    [Teardown]    logout and close browser

*** Keywords ***
open browser and login
    open_login_url
    sleep3s
    input_username    ${username}
    input_password    ${password}
    click_login
    sleep3s

open browser and login1
    [Arguments]    ${username1}    ${password1}
    open_login_url
    sleep3s
    input_username    ${username1}
    input_password    ${password1}
    click_login
    sleep3s
    logout and close browser
