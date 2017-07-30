*** Settings ***
Resource          公共关键字.robot
Resource          业务关键字.robot

*** Test Cases ***
新增联系人
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[5]/a
    Sleep    1s
    Click Element    xpath=//*[@id='menuActions']/a
    Input Text    xpath=//*[@id='realname']    张三
    Click Element    xpath=//*[@id='maker']
    Click Element    xpath=//*[@id='newCustomer']
    ${mytime}=    Get Time
    Input Text    xpath=//*[@id='name']    ${mytime}
    Click Element    xpath=//*[@id='submit']

删除联系人
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[5]/a
    Sleep    1s
    Click Element    xpath=//*[@id='contactList']/tbody/tr/td[8]/div/a
    Sleep    1s
    Click Element    xpath=//*[@id='contactList']/tbody/tr/td[8]/div/ul/li[2]/a
    Dismiss Alert

删除客户
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    xpath=//*[@id='mainNavbar']/div[2]/ul/li[4]/a
    Click Element    xpath=//*[@id='ajaxForm']/table/tbody/tr[1]/td[11]/div/a
    Sleep    1s
    Click Element    xpath=//*[@id='ajaxForm']/table/tbody/tr[1]/td[11]/div/ul/li[4]/a
    Dismiss Alert

增加客户
    管理员登陆成功    admin    admin8888    退出
    进入客户管理的frame
    Click Element    //*[@id='mainNavbar']/div[2]/ul/li[4]/a
    Click Element    //*[@id='menuActions']/a
    ${mytime}=    Get time
    Input Text    //*[@id='name']    ${mytime}
    Input Text    //*[@id='contact']    张三
    Click Element    //*[@id='submit']
