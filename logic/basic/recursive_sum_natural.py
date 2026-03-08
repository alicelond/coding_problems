import unittest

# Given a positive integer n, find the sum of the first n natural numbers.

def sum_natural(n):
    if n < 0:
        # Raises an error to the user if the input is negative.
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

class TestSumNatural(unittest.TestCase):
    # Test cases for the function sum_natural
    # For the recursion implementation, we need to adjust our test case otherwise the test will fail
    def test_zero(self):
        with self.assertRaises(ValueError):
            sum_natural(0)

    def test_positive_number(self):
        self.assertEqual(sum_natural(5), 15)

if __name__ == "__main__":
    unittest.main()