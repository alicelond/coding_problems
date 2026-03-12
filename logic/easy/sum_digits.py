import unittest

# Given a number n, find the sum of its digits.

def sum_digits(n):
    sum = 0

    while(n > 0):
        remainder = n % 10
        n = n // 10 
        sum += remainder
    return sum

class TestSumDigits(unittest.TestCase):
    def test_sum_digits(self):
        self.assertEqual(sum_digits(687), 21)
        self.assertEqual(sum_digits(12), 3)

if __name__ == '__main__':
    unittest.main()