*** Settings ***
Resource          业务关键字.robot
Resource          公共关键字.robot

*** Test Cases ***
管理员创建张三用户
    [Template]
    管理员登陆成功    admin    admin8888    退出
    跳转到创建用户并填写数据
    删除用户

登录并删除张三用户
    管理员登陆成功    admin    admin8888    退出
    删除用户

*** Keywords ***
