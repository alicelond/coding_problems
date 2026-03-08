import unittest

# Given a positive integer n, we have to find the sum of squares of first n natural numbers.

def sum_of_squares(n):
    # We can use Faulhaber's formula to calculate the sum of squares in O(1) time.
    if n < 0:
        raise ValueError("Input must be a positive integer.")
    return n * (n + 1) * (2 * n + 1) // 6

class TestSumOfSquares(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sum_of_squares(0), 0)

    def test_positive_number(self):
        self.assertEqual(sum_of_squares(8), 204)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sum_of_squares(-5)

if __name__ == "__main__":
    unittest.main()