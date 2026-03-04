# Testing Strategy

This project uses both unit testing and integration testing to verify the functionality of the Quick-Calc calculator.

## What Was Tested

The following aspects of the application were tested:

- Addition operation
- Subtraction operation
- Multiplication operation
- Division operation
- Division by zero handling
- Negative number calculations
- Decimal number calculations
- Large number calculations
- Interaction between the input processing layer and calculator logic
- Clear function to reset the calculator

## Testing Pyramid

The testing approach follows the Testing Pyramid concept. The majority of the tests in this project are unit tests because they are fast and verify small parts of the application logic. A smaller number of integration tests are used to ensure that the interaction between the input processing layer and the calculator logic works correctly.

## Black-box vs White-box Testing

Unit tests follow a white-box testing approach because they directly test the internal methods of the Calculator class.

Integration tests are closer to black-box testing because they simulate user interactions with the application interface without focusing on the internal implementation.

## Functional vs Non-Functional Testing

This project focuses mainly on functional testing to verify that calculator operations produce correct results.

Non-functional aspects such as performance, usability, and security were not tested because they are outside the scope of this small application.

## Regression Testing

The test suite can also be used for regression testing. If future updates modify the calculator logic, running the test suite will quickly detect if any previously working functionality has broken.

## Test Results Summary

| Test Name | Type | Result |
|-----------|------|--------|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_full_calculation | Integration | Pass |
| test_clear_function | Integration | Pass |
