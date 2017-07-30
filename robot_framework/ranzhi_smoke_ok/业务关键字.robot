*** Settings ***
Resource          公共关键字.robot
Library           Selenium2Library

*** Keywords ***
管理员登陆成功
    [Arguments]    ${username}    ${password}    ${flag}
    打开浏览器并转到登录页面
    输入用户名和密码    ${username}    ${password}
    点击登录按钮
    验证登录成功    ${flag}

跳转到创建用户并填写数据
    Click Element    //*[@id='s-menu-superadmin']/button
    Select Frame    id=iframe-superadmin
    Click Element    //*[@id='shortcutBox']/div/div[1]/div/a/h3
    Input Text    //*[@id='account']    zhangsan
    Input Text    //*[@id='realname']    张三
    Click Element    //*[@id='gender1']
    Select From List By Index    //*[@id='role']    10
    Input Password    //*[@id='password1']    123456
    Input Password    //*[@id='password2']    123456
    Input Text    //*[@id='email']    12345@qq.com
    Click Element    //*[@id='submit']

删除用户
    Click Element    //*[@id='s-menu-superadmin']/button
    Select Frame    id=iframe-superadmin
    Click Element    //*[@id='mainNavbar']/div[2]/ul/li[2]/a
    Click Element    xpath=html/body/div[1]/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]
    Dismiss Alert
