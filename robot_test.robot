*** Settings ***
Library    RequestsLibrary

*** Variables ***
${API_URL}    http://192.168.17.133:5000/is_prime/

*** Test Cases ***
Test When X Is 17
    [Documentation]    Test that the API returns true when x is 17
    Create Session    My Session    ${API_URL}
    ${response}    GET On Session    My Session    /17
    Should Be Equal As Strings    ${response.text}    True


Test When X Is 36
    [Documentation]    Test that the API returns false when x is 36
    Create Session    My Session    ${API_URL}
    ${response}    GET On Session   My Session    /36
    Should Be Equal As Strings    ${response.text}    False


Test When X Is 13219
    [Documentation]    Test that the API returns true when x is 13219
    Create Session    My Session    ${API_URL}
    ${response}    GET On Session    My Session    /13219
    Should Be Equal As Strings    ${response.text}    True

