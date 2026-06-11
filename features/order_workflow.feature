Feature: End To End Order Workflow

  Scenario: Verify complete order placement workflow

    Given User is on login page

    When User logs into application

    And User adds product to cart

    And User proceeds to checkout

    And User places the order

    Then Generated order should exist in order history