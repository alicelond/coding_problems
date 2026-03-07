import unittest
# Given a number n, check whether it is even or odd. 
# Return true for even and false for odd.

def is_even(n):
    # The last bit of an even number is always 0, while the last bit of an odd number is always 1.
    # If we perform a bitwise AND operation between n and 1, we can determine if n is even or odd.

    # Example: 15 & 1 = 1111 & 0001 = 0001 (odd)
    # Example: 14 & 1 = 1110 & 0001 = 0000 (even)
    if (n & 1) == 0:
        return True
    else:        
        return False

class TestIsEven(unittest.TestCase):
    # Test cases for the function is_even
    def test_even_number(self):
        self.assertTrue(is_even(4))
    def test_odd_number(self):
        self.assertFalse(is_even(5))
    
if __name__ == "__main__":
    unittest.main()