Feature: Critical test scenarios of getting gists

  @priority-High
  Scenario: Get a public gist of another user, ensure gist is successfully fetched
    Given I have valid Github API Gist token
    When I get the list of public gists
    Then Response status should be 200
    And Gists should be listed
    When I select a random public gist and go to its detail
    Then Gist data should be in the response

  @priority-High
  Scenario: Ensure gist is accessible by id with valid token
    Given I have valid Github API Gist token
    When I get gist with id
    Then Gist data should be in the response

  @priority-High @negative
  Scenario: Ensure gist is not accessible by id with fake-invalid token, 401 should return
    Given I have invalid Github API Gist token
    When I get gist with id
    Then Response status should be 401
    And Error message should contain Bad credentials


  @priority-High
  Scenario: Ensure gist is accessible by id without token, not logged in users
    Given I have no Github API Gist token
    When I get gist with id
    Then Gist data should be in the response

  @priority-High
  Scenario: Ensure gist is accessible by id with a token that doesn't have permission for gists
    Given I have without_permission Github API Gist token
    When I get gist with id
    Then Gist data should be in the response

  @priority-High
  Scenario: Ensure public gists list is accessibility by different tokens
    Given I have valid Github API Gist token
    When I get the list of public gists
    Then Response status should be 200
    And Gists should be listed

    Given I have no Github API Gist token
    When I get the list of public gists
    Then Response status should be 200
    And Gists should be listed

    Given I have without_permission Github API Gist token
    When I get the list of public gists
    Then Response status should be 200
    And Gists should be listed

    Given I have invalid Github API Gist token
    When I get the list of public gists
    Then Response status should be 401
    And Error message should contain Bad credentials


  @priority-High
  Scenario: Get the list of public gists ensure no private gist appeared
#  This scenario has a flaw, as critical we can check first 30 gists if all is needed it'll increase run time
    Given I have valid Github API Gist token
    When I get the list of public gists
    Then Gists should be listed
    And No private gist should appear on public gists list

  @priority-Medium @negative
  Scenario: Retrieve a gist with Non-Existed Id
    Given I have valid Github API Gist token
    When I try to retrieve non-existing gist id
    Then Response status should be 404
    And Error message should contain Not Found

