Feature: test home page
Background:
  Given go to home page

  Scenario: test checked in home check box
    Given go to check box page
    And click on check all
    Then check status of all children check boxes


