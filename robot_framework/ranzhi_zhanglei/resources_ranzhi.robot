*** Settings ***
Library           Selenium2Library
Library           DateTime

*** Variables ***
${server}         192.168.2.7/ranzhi/www
${browser}        chrome
${username}       admin
${password}       admin8888
${login_success}    http://${server}/sys/index.html
${login_url}      http://${server}/

*** Keywords ***
open_login_url
    Open Browser    ${login_url}    ${browser}
    #Maximize Browser Window

input_username
    [Arguments]    ${username1}
    Input Text    id = account    ${username1}
    #Input Text    id = accout type = text    ${username1}

input_password
    [Arguments]    ${password1}
    Input Text    id = password    ${password1}

click_login
    Click Button    id= submit

sleep3s
    sleep    3s

logout and close browser
    sleep    2s
    Click Button    id=start
    sleep    2s
    Click Element    xpath = .//*[@id='startMenu']/li[10]/a
    sleep    2s
    Close All Browsers

jump OA
    Click Button    xpath=.//*[@id='s-menu-2']/button
    sleep    1s

跳转oa项目页面
    Click Link    xpath=.//*[@id='mainNavbar']/div[2]/ul/li[2]/a
    sleep    1s

input_project_information
    Input Text    id=name    project1
    Input Text    id=begin    2017-07-30
    Input Text    id=end    2017-08-30
    Select Frame    xpath=.//*[@id='ajaxForm']/table/tbody/tr[6]/td/div/div[2]/iframe
    Input Text    xpath=html/body    项目描述
    Unselect Frame
    Comment    Click Button    xpath=.//*[@id='leftBar']
    select Frame    id=iframe-2
    Select Checkbox    id=whitelist1
    sleep    1s
    Select Checkbox    id=whitelist2
    sleep    1s
    unSelect Checkbox    id=whitelist1
