*** Settings ***
Library           String
Library           Selenium2Library
Library           requests
Library           OperatingSystem
Resource          resources.robot
Library           Process
Library           Collections
Resource          mysource.robot
Library           Screenshot

*** Variables ***
${a}              abcd
@{list_var1}      abc    def    123
${b}              dddd
&{user1}          username=admin    password=123456
${CUR_DIR}        F:\\GitHub\\robot_framework\\Learn_RIDE\\

*** Test Cases ***
case0_log
    log    ${a}
    log    ${b}
    log many    @{list_var1}
    log many    &{user1}

case1_log
    [Tags]    logtest
    set log level    trace
    Log    hello <b>world!</b> debug    level=warn    html=yes    console=yes
    log    info message    level=info    html=yes    console=yes
    log    error message    level=error    html=yes    console=yes

case2_add_Library
    [Documentation]    在测试套的settings里可以添加 Library，按F5可以查看函数帮助文档
    log    演示如何添加Library

case3_add_Resource
    [Documentation]    添加资源，注意路径，如果是同一个目录，直接写文件全名（包括扩展名）。
    ...    如果是其他目录，注意使用../之类的操作定位到目录（相对路径）
    log    ${username}
    log    ${passwd}
    log    ${location}

case4_Add_Scalar_List
    [Documentation]    在测试套（suite）里设置变量
    log    ${a}    #注释
    log    这是${a}例子
    #log    @{list_var1}    #这是错误的
    log many    @{list_var1}
    @{name_list1}    Set Variable    wang    jin ling
    log many    @{name_list1}
    @{name_list2}    create list    wang    jin ling
    log many    @{name_list2}
    @{login_info}    create list    ${username}    ${passwd}
    log many    @{login_info}
    @{num_string}    Create List    ${3.14}    u'3.14'
    log many    @{num_string}
    #注意log many的用法
    #开头的都是注释，比如这一条

case5_系统常量
    [Documentation]    系统常量必须以%开头。
    ...    常量主要有环境变量、数值常量、特殊字符常量、系统保留常量
    ...
    ...    注意：对系统常量，只能使用，不能赋值
    log    %{path}
    log    %{tmp}
    log    %{ANDROID_HOME}
    log    %{JAVA_HOME}

case6_Add_Dict
    [Documentation]    Dict的值
    #演示Dict的用法
    &{dict_a}    Create Dictionary    first=1    second=2    third=3
    log many    &{dict_a}

case7_Number_元组
    [Documentation]    生成list的时候，第一个是数字类型，第二个是字符串类型
    ${int_num}    Set Variable    ${12}    #int
    ${float_num}    Set Variable    ${3.14}    #float
    @{list_num1}    set variable    ${3.14159}    '3.14'
    ${scalar_a}    set variable    username
    ${tuple}    Set Variable    ${1,2}
    ${test_space}    set variable    '${SPACE*4}'
    ${string}    Set Variable    '123456'
    log    ${string}
    ${SPACE}

case8_变量赋值_if条件
    [Documentation]    注意：这个用例定义的 ${var1} 和 ${var2} 只能在本TestCase里使用
    ${var1}=    set variable    abcd
    ${var2}=    set variable if    '${var1}' == 'abcd'    if条件成立    if条件不成立
    log many    ${var1}    ${var2}
    Run Keyword if    '${var1}' == 'abcd'    log    if条件成立

case9_Get赋值_获取当前时间
    ${var3}    Get Length    ${a}
    log    ${var3}
    ${cur_time}    Get Time
    ${dd}=    evaluate    '${cur_time}'[0:11]
    ${dd1}=    Fetch From Left    ${cur_time}    ${SPACE}
    ${date}    Get Time    year,month,day

case10_命令行赋值
    [Documentation]    演示从命令行赋值，
    log    ${var30}

case11_Scalar变量使用_IF条件
    Run Keyword If    '${a}' == 'abcd'    log    log执行成功
    #关键字的使用
    log    字符串连接${a}完成
    log    ${a[0:2]}
    ${tmp}=    evaluate    '${a}'[0:2]
    log    ${a[1]}
    Comment    列表的切片
    ${num1}=    set variable    ${123}
    ${num2}=    evaluate    ${num1}+1
    log    ${num2}
    @{list4}    create list    ${123}    u'123'    123
    #evalute的作用实际上是把表达式放到Python里运行    Convert To Integer
    #evalute是重点

case12_Scalar高级用法
    ${var1}    ${var2}=    set variable    hello    world
    #注意这种赋值方法
    log    ${var1}${SPACE}${var2}

case13_List变量
    @{var1}=    set variable    1    2    3
    @{var2}    create list    a    b    c
    log many    @{var1}    @{var2}
    run keyword    log    ${a}    WARN
    Comment    log    ${a}    WARN
    #下面是方法二
    @{argVal3}    create list    abcd    WARN
    ${keyword}    set variable    log
    run keyword    ${keyword}    @{argVal3}
    #获取list的值
    log    @{var1}[1]    #方法一
    log    ${var1[1]}    #方法二也可以，个人不建议使用
    @{var3}    create list    @{var1}    @{var2}    #合并两个list为1个list
    @{var4}    create list    ${var1}    ${var2}    #新建一个二维list
    log    @{var4[0]}[1]
    ${tmp2}=    evaluate    @{var4}[0][1]

case14_For循环
    : FOR    ${i}    IN RANGE    10
    \    LOG    i=${i}
    : FOR    ${i}    IN RANGE    3    8    2
    \    LOG    i=${i}
    @{listVal}    Create List    1    2    F
    : FOR    ${n}    IN    @{listVal}
    \    log    n=${n}

case15_标准库截图
    Screenshot.Set Screenshot Directory    c:\Intel
    sleep    2s
    Take Screenshot    mypic
    Take Screenshot    mypic

case15_Selenium截图
    open Browser    https://www.baidu.com    chrome
    ${file1} =    Capture Page Screenshot
    log    ${OUTPUT_DIR}
    File Should Exist    ${OUTPUT_DIR}${/}selenium-screenshot-1.png
    File Should Exist    ${file1}
    ${file2}    Capture Page Screenshot
    File Should Exist    ${OUTPUT_DIR}${/}selenium-screenshot-2.png
    File Should Exist    ${file2}
    close Browser

case16_collections
    ${tuple}    Evaluate    (u'woody', u'pecker')
    @{list}    convert to list    ${tuple}
    @{tmp}    create list    1    2
    log    ${tmp}
    append to list    ${list}    is    best
    log    ${list}
    insert into list    ${list}    1    good
    log    ${list}
    ${last_elem}    get from list    ${list}    -1
    ${get_by_index}    get index from list    ${list}    good
    log many    @{list}
    &{dict}    Create Dictionary    a=1    b=2
    Set To Dictionary    ${dict}    a=3    c=4
    Log Dictionary    ${dict}
    Remove From Dictionary    ${dict}    a
    Log Dictionary    ${dict}

case17_File文件操作
    [Documentation]    Create File，创建文件，指定文件内容；
    ...    Get File 获得文件的内容；
    ...    Get File Size获取文件的大小；
    ...    Grep File在文件内容中搜索特定的关键字的行；
    ...    Touch 是类似于Linux的Touch，作用是创建一个空文件或者修改文件的时间戳；
    ...    Remove Files就是删掉这些文件
    log    ${CUR_DIR}
    Create File    ${CUR_DIR}file.txt    测试数据
    ${file_content}    Get File    ${CUR_DIR}file.txt
    ${file_size}    Get File Size    ${CUR_DIR}file.txt
    Append To File    ${CUR_DIR}file.txt    \r\n中国人民很伟大\r\n勤劳
    ${grep_line}    Grep File    ${CUR_DIR}file.txt    伟大
    Touch    ${CUR_DIR}touch.txt
    Remove Files    ${CUR_DIR}touch.txt    ${CUR_DIR}file.txt

case20_process操作
    ${result}    Run process    python    -c    print "robot"
    log    ${result.stdout}
    Run process    python    -c    print "rf"    alias=rf
    ${p_result}    Get Process Result    rf
    start process    python    alias=py2
    start process    ping    alias=ping
    switch process    py2
    Comment    terminate all processes
