Feature: Critical test scenarios of creating different type of gists

  @priority-High
  Scenario: Create a successful simple PRIVATE gist and check if it successfully created
    Given I have valid Github API Gist token
    When I create a private gist containing txt type files
    Then Response status should be 201
    And Gist data should be in the response
    When I retrieve the gist
    Then Created gist details should match the original input


  @priority-High
  Scenario: Create a successful simple PUBLIC gist and check if it successfully created
    Given I have valid Github API Gist token
    When I create a public gist containing txt type files with PublicTestGist as description
    Then Response status should be 201
    And Gist data should be in the response
    When I retrieve the gist
    Then Created gist details should match the original input

  @priority-High @negative
  Scenario: Try to create a gist without token and ensure 401 returned
    Given I have no Github API Gist token
    When I create a private gist containing txt type files
    Then Response status should be 401
    And Error message should contain Requires authentication
    When I create a public gist containing txt type files
    Then Response status should be 401
    And Error message should contain Requires authentication

  @priority-High @negative
  Scenario: Try to create a gist with invalid token and ensure 403 returned
    Given I have invalid Github API Gist token
    When I create a private gist containing txt type files
    Then Response status should be 403
    And Error message should contain Resource not accessible
    When I create a public gist containing txt type files
    Then Response status should be 403
    And Error message should contain Resource not accessible

