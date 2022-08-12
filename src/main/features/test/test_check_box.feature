Feature: test home page
Background:
  Given go to home page

  Scenario Outline: test text box with valid email
    Given go to text box page
    And input Full Name <full_name>
    And input Email <email>
    And input Current Address <current_address>
    And input Permanent Address <permanent_address>
    And click submit button
    Then check value get from text area
  Examples:
    | full_name      | email            | current_address   | permanent_address   |
    | dang dinh ngoc | ngocdd@gmail.com | Cau Giay          | Ha Noi              |
    | ho ten | hehe@gmail.com | asdasd | asdasdd |

  Scenario Outline: test text box with invalid email
    Given go to text box page
    And input Full Name <full_name>
    And input invalid Email <email>
    And input Current Address <current_address>
    And input Permanent Address <permanent_address>
    And click submit button
    Then check validate wrong email
  Examples:
    | full_name      | email            | current_address   | permanent_address   |
    | dang dinh ngoc | day la email | Cau Giay          | Ha Noi              |
