*** Settings ***
Resource          业务关键字.robot

*** Test Cases ***
张三登录
    [Template]
    管理员登陆成功    zhangsan    123456    退出
