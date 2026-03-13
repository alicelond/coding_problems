import unittest

# Given a positive integer, check if the number is prime or not. 
# A prime is a natural number greater than 1 that has no positive divisors other 
# than 1 and itself. Examples of the first few prime numbers are {2, 3, 5, ...}
# Input:  n = 11 Output: true
# Input:  n = 15 Output: false

def prime_test(n):
    if n <= 1:
        return False
    
    # Check from 2 to n-1 because range is exclusive of the last number
    for i in range(2, n):
        if n % i == 0:
            return False
    # If it doesn't fit the criteria, it's prime    
    return True
        
class TestPrimeTest(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(prime_test(1), False)
        self.assertEqual(prime_test(11), True)
        self.assertEqual(prime_test(15), False)

if __name__ == '__main__':
    unittest.main()