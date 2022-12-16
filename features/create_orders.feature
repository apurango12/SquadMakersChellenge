Feature: CREATE ORDERS
  As a user, I should be able to create orders and complete the checkout flow

  Scenario: Buy two items
    Given Im in the main page
    When Select the two products in the menu
    And Complete the checkout
    Then The products are bought successfully

