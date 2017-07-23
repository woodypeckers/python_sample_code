*** Settings ***
Documentation     resource.robot 灰色是因为没有被引用

*** Variables ***
${username}       admin    # 管理员的账户
${passwd}         123456
&{dict_aa}        key1=value1    key2=value2
@{list_aa}        hello    world    byebye    world
