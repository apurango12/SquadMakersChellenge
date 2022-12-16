Feature: LOGIN
  As a user, I should be able to login to my account

  Scenario: Login with valid credential
    Given Go to the website
    When  User logs in with valid credential
    Then  I should be logged in successfully



  Scenario: Login with invalid credential
    Given Go to the website
    When Fill invalid username and password
    Then I should get an error message


  Scenario: Logout
    Given Im in the main page
    When Go to the dropdown menu
    And hit the logout button
    Then The application logged out successfully
