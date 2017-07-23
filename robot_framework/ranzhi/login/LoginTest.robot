*** Settings ***
Library           Selenium2Library

*** Test Cases ***
admin_login_logout
    open browser    http://123.207.97.109/autotest/ranzhi/www/sys/index.php
    Delete All Cookies
    Wait Until Page Contains    阿里巴巴公司
    Input text    name=account    admin
    input text    name=password    admin8888
    Click Button    id=submit
    Wait Until Page Contains
    Page Should Contain    所有应用
    ${title}    get title
    log    ${title}
    Close Browser
