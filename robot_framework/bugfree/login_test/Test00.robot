*** Settings ***
Library           Selenium2Library

*** Test Cases ***
login_suceess
    Open Browser    http://localhost/bugfree    ie    bugfree
    Input Text    id=LoginForm_username    admin
    Input Text    id=LoginForm_password    123456
    Click Button    id=SubmitLoginBTN
    Sleep    3s
    ${title}=    Get Title
    Should Contain    ${title}    BugFree

login_fail_invalid_username
    Open Browser    http://localhost/bugfree    ie    bugfree
    Input Text    id=LoginForm_username    invalid
    Input Text    id=LoginForm_password    123456
    Click Button    id=SubmitLoginBTN
    Sleep    3s
    ${title}=    Get Title
    Should Contain    ${title}    BugFree
