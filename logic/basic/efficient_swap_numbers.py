import unittest

#Given two numbers a and b, the task is to swap them. 
# Examples: Input: a = 2, b = 3
# Output: a = 3, b = 2

def swap_numbers(a, b):
    # Use bitwise XOR to swap the values of a and b without using a temporary variable
    # nor using tuple unpacking. 
    a = a ^ b # a now holds the result of a XOR b
    b = a ^ b # b now holds the original value of a (since a XOR b XOR b = a)
    a = a ^ b # a now holds the original value of b (since a XOR b XOR a = b)
    return a,b

class TestSwapNumbers(unittest.TestCase):
    def test_swap_numbers(self):
        self.assertEqual(swap_numbers(2, 3), (3, 2))
        self.assertEqual(swap_numbers(-1, 5), (5, -1))
        self.assertEqual(swap_numbers(0, 0), (0, 0))

if __name__ == "__main__":
    unittest.main()