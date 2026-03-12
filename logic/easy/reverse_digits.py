import unittest

# Given an Integer n, find the reverse of its digits.
# Input: n = 12345 Output: 54321

def reverse_digits(n):
    reverse = 0 

    while(n > 0):
        remainder = n % 10
        n = n // 10
        reverse = remainder + (reverse * 10)
    return reverse

class TestReverseDigits(unittest.TestCase):
    def test_reverse_digits(self):
        self.assertEqual(reverse_digits(12345), 54321)
        self.assertEqual(reverse_digits(987654321), 123456789)

if __name__ == '__main__':
    unittest.main()