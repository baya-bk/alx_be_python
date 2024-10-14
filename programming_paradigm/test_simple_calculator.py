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
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(5, -5), -25)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-10, 5), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)

        # Test division by zero (expecting None)
        self.assertIsNone(self.calc.divide(10, 0),
                          "Expected None when dividing by zero")

    def test_edge_cases(self):
        """Test edge cases for all operations."""
        # Test subtracting a number from itself
        self.assertEqual(self.calc.subtract(5, 5), 0)

        # Test multiplying by zero
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

        # Test dividing zero by a number
        self.assertEqual(self.calc.divide(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
