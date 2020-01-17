# Generate a unittest for basic_functions.py

import unittest
from basic_functions import factorial


class RoundTests(unittest.TestCase):
    """Test factorial function."""
    def test_factorial6(self):
        self.assertEqual(factorial(6), 720)

    def test_factorial1(self):
        self.assertEqual(factorial(1), 1)


if __name__ == '__main__':
    unittest.main()
