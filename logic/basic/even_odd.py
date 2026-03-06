import unittest
# Given a number n, check whether it is even or odd. 
# Return true for even and false for odd.

def is_even(n):
    if n % 2 == 0:
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