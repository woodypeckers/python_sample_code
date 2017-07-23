*** Settings ***
Suite Teardown    Delete All Sessions
Library           Collections
Library           String
Library           OperatingSystem
Library           RequestsLibrary

*** Test Cases ***
Get Requests
    [Tags]    get
    Create Session    google    http://www.google.com
    Create Session    github    https://api.github.com
    ${resp}=    Get Request    google    /
    Should Be Equal As Strings    ${resp.status_code}    200
    ${resp}=    Get Request    github    /users/bulkan
    Should Be Equal As Strings    ${resp.status_code}    200
    Dictionary Should Contain Value    ${resp.json()}    Bulkan Evcimen

Get Requests with Url Parameters
    [Tags]    get
    Create Session    httpbin    http://httpbin.org
    &{params}=    Create Dictionary    key=value    key2=value2
    ${resp}=    Get Request    httpbin    /get    params=${params}
    Should Be Equal As Strings    ${resp.status_code}    200
    ${jsondata}=    To Json    ${resp.content}
    Should be Equal    ${jsondata['args']}    ${params}

Get Requests with Json Data
    [Tags]    get
    Create Session    httpbin    http://httpbin.org
    &{data}=    Create Dictionary    latitude=30.496346    longitude=-87.640356
    ${resp}=    Get Request    httpbin    /get    json=${data}
    Should Be Equal As Strings    ${resp.status_code}    200
    ${jsondata}=    To Json    ${resp.content}
    Should Be Equal As Strings    ${resp.status_code}    200

Get HTTPS & Verify Cert
    [Tags]    get
    Create Session    httpbin    https://httpbin.org    verify=True
    ${resp}=    Get Request    httpbin    /get
    Should Be Equal As Strings    ${resp.status_code}    200
