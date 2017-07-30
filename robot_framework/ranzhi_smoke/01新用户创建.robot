*** Settings ***
Resource          业务关键字.robot
Resource          公共关键字.robot

*** Test Cases ***
管理员创建李四用户
    [Template]
    管理员登陆成功    admin    admin8888    退出
    转到    http://192.168.2.7/ranzhi/www/sys/admin/
    Select Frame    id=iframe-superadmin
    Click Link    添加成员
    Input Text    id=account    lisi
    Input Text    id=realname    李四
    Select Radio Button    gender    gender1
    Select From List By Value    id=role    pm
    Input Password    id=password1    123456
    Input Password    id=password2    123456
    Input Text    id=email    lisi@qq.com
    Click Element    id=submit
    unSelect Frame
    删除李四用户

管理员创建李四用户_用户名格式错误
    [Template]
    管理员登陆成功    admin    admin8888    退出
    转到    http://192.168.2.7/ranzhi/www/sys/admin/
    Select Frame    id=iframe-superadmin
    Click Link    添加成员
    Input Text    id=account    李四
    Input Text    id=realname    李四
    Select Radio Button    gender    gender1
    Select From List By Value    id=role    pm
    Input Password    id=password1    123456
    Input Password    id=password2    123456
    Input Text    id=email    lisi@qq.com
    Click Element    id=submit
    unSelect Frame

删除李四用户
    管理员登陆成功    admin    admin8888    退出
    转到    http://192.168.2.7/ranzhi/www/sys/admin/
    删除李四用户

*** Keywords ***
特定的逻辑

删除李四用户
    Sleep    2s
    select frame    id=iframe-superadmin
    Click Link    组织
    Page Should Contain    李四
    unselect frame
    sleep    1s
    select frame    id=iframe-superadmin
    Click Element    xpath=/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]
    sleep    2s
    Confirm Action
