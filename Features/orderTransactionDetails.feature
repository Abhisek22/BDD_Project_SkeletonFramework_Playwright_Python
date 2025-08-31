Feature: Order Transaction Details
    Tests related to Order Transactions


  Scenario Outline: Verify Order success message shown in details page
    Given Through API place the item order with <username> and <password>
    When I login to portal with <username> and <password>
    And Navigate to orders page
    And Select the orderId
    Then Order message is successfully displayed
    Examples:
      | username                   | password    |
      | abhisekghosh22@gmail.com   | Password123 |
      | rahulshetty@gmail.com      | Iamking@000 |

