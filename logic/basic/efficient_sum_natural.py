import unittest

# Given a positive integer n, find the sum of the first n natural numbers.

def sum_natural(n):
    # The efficient approach considers the formula of the Gaussian sum:
    # sum = (n * (n + 1)) / 2
    return (n * (n + 1)) // 2

class TestSumNatural(unittest.TestCase):
    # Test cases for the function sum_natural
    def test_zero(self):
        self.assertEqual(sum_natural(0), 0)

    def test_positive_number(self):
        self.assertEqual(sum_natural(5), 15)

if __name__ == "__main__":
    unittest.main()