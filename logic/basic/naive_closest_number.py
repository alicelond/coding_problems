import unittest

# Given two integers n and m (m != 0). Find the number closest to n and divisible by m.
#  If there is more than one such number, then output the one having maximum absolute value.

def closest_number(n, m):
    if (m == 0):
        raise ValueError("m cannot be zero")

    # Checks if n is divisible by m
    if (n % m == 0):
        return n
    right_number = n + 1
    left_number = n - 1

    # Checks for the closest number on the right side of n which is divisible by m
    while (right_number % m != 0):
        right_number += 1

    # Checks for the closest number on the left side of n which is divisible by m
    while (left_number % m != 0):
        left_number -= 1
    
    distance_right = right_number - n
    distance_left = n - left_number

    if (distance_right == distance_left):
        # We use key=abs so that max compares values using their absolute values
        return max(left_number, right_number, key=abs)
    elif (distance_left < distance_right):
        return left_number
    else:
        return right_number

class TestClosestNumber(unittest.TestCase):
    def test_zero(self):
        with self.assertRaises(ValueError):
            closest_number(5, 0)
    def test_positive_numbers(self):
        self.assertEqual(closest_number(13,4), 12)
    def test_negative_numbers(self):
        self.assertEqual(closest_number(-15,6), -18)

if __name__ == "__main__":
    unittest.main()