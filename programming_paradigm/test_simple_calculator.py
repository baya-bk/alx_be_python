import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = self.calc.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        # Test normal division
        result = self.calc.divide(10, 5)
        self.assertEqual(result, 2)

        # Test division by zero (expecting None)
        result = self.calc.divide(10, 0)
        self.assertIsNone(result, "Expected None when dividing by zero")

    def test_edge_cases(self):
        # Test subtracting a number from itself
        result = self.calc.subtract(5, 5)
        self.assertEqual(result, 0)

        # Test multiplying by zero
        result = self.calc.multiply(10, 0)
        self.assertEqual(result, 0)

        # Test dividing zero by a number
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
