Feature: Critical test scenarios of getting different type of gists

@priority:High
  Scenario: Get a public gist of another user, ensure gist is successfully fetched
    Given I have valid Github API Gist token
    When I get the list of public gists
    Then Response status should be 200
    And Gists should be listed
    When I select a random public gist and go to its detail
    Then Gist data should be in the response

@priority:High
  Scenario: Ensure gist is accessible by id with valid token
    Given I have valid Github API Gist token
    When I get gist with id
    Then Gist data should be in the response

@priority:High
  Scenario: Ensure gist is accessible by id with invalid token
    Given I have invalid Github API Gist token
    When I get gist with id
    Then Gist data should be in the response

@priority:High
  Scenario: Try to get a gist by id without token, not logged in users
    Given I have no Github API Gist token
    When I get gist with id
    Then Gist data should be in the response

@priority:High
  Scenario: Ensure public gists list is accessible by anyone
    Given I have invalid Github API Gist token
    When I get the list of public gists
    Then Response status should be 200
    And Gists should be listed
    Given I have valid Github API Gist token
    When I get the list of public gists
    Then Response status should be 200
    And Gists should be listed
    Given I have no Github API Gist token
    When I get the list of public gists
    Then Response status should be 200
    And Gists should be listed


@priority:High
  Scenario: Get the list of public gists ensure no private gist appeared
#  This scenario has a flaw, as critical we can check first 30 gists if all is needed it'll increase run time
    Given I have valid Github API Gist token
    When I get the list of public gists
    Then Gists should be listed
    And No private gist should appear on public gists list

@priority:Medium @negative
  Scenario: Retrieve a gist with Non-Existed Id
    Given I have valid Github API Gist token
    When I try to retrieve non-existing gist id
    Then Response status should be 404
    And Error message should contain Not Found

