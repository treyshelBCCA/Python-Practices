import unittest
from main import calculate_discounted_price

class TestCalculateDiscountedPrice(unittest.TestCase):

    def test_discounted_price(self):
        # Test case 1: Normal scenario
        self.assertAlmostEqual(calculate_discounted_price(100.0, 10.0), 90.0, delta=0.01)

        # Test case 2: Zero original price
        self.assertAlmostEqual(calculate_discounted_price(0.0, 20.0), 0.0, delta=0.01)

        # Test case 3: Zero discount
        self.assertAlmostEqual(calculate_discounted_price(50.0, 0.0), 50.0, delta=0.01)

        # Test case 4: Rounding behavior
        self.assertAlmostEqual(calculate_discounted_price(99.99, 15.0), 84.99, delta=0.01)

if __name__ == '__main__':
    unittest.main()
