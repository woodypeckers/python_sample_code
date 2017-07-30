*** Settings ***
Resource          公共关键字.robot

*** Keywords ***
管理员登陆成功
    [Arguments]    ${username}    ${password}    ${flag}
    打开浏览器并转到登录页面
    输入用户名和密码    ${username}    ${password}
    点击登录按钮
    验证登录成功    ${flag}
