*** Settings ***
Library           Selenium2Library

*** Variables ***
${base_url}       http://localhost/ranzhi/www
&{admin_info}     username=admin    password=123456    job=admin
&{sales_manager}    username=sale1    password=123456    job=销售经理    gender=男

*** Keywords ***
打开浏览器并转到登录页面
    Open Browser    ${base_url}    Chrome
    Set Browser Implicit Wait    10s

输入用户名和密码
    [Arguments]    ${username}    ${password}
    Input Text    id=account    ${username}
    Input Password    id=password    ${password}

点击登录按钮
    Click Element    id=submit

验证登录成功
    [Arguments]    ${flag}
    Page Should Contain    ${flag}

关闭浏览器
    Close Browser

转到
    [Arguments]    ${url}
    go to    ${url}

进入客户管理的frame
    Click Element    xpath=//*[@id='s-menu-1']/button
    Select Frame    id=iframe-1
