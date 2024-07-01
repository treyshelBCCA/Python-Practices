# Python Practice: Unit Testing

## Objective

This exercise aims to help you learn how to write unit tests in Python using the `unittest` framework. You will create test cases to validate the functionality of a simple Python function for calculating discounted prices.

## Requirements

1. **Function to Test**

   Implement a function `calculate_discounted_price(original_price: float, discount: float) -> float` that calculates the discounted price based on the original price and discount percentage. The function should return the discounted price rounded to two decimal places.

2. **Unit Tests**

   Write unit tests using the `unittest` framework to validate the correctness of the `calculate_discounted_price` function. Include tests for different scenarios such as:

   - Calculating discounted price with various original prices and discounts.
   - Handling edge cases like zero discount or zero original price.
   - Testing the rounding behavior of the discounted price.
