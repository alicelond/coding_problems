import unittest 

# Given two integers n and m (m != 0). Find the number closest to n and divisible by m.
#  If there is more than one such number, then output the one having maximum absolute value.

def closest_number(n, m):
    if (m == 0):
        raise ValueError("m cannot be zero")
    
    # This implementation uses the Euclidean division theorem n = m * q + r
    q = n // m

    n1 = m * q # First candidate

    if ((n and m > 0) or (n and m < 0)):
        n2 = m * (q + 1) # We're searching for closest multiple above n, n2 is second candidate
    else:
        n2 = m * (q - 1) # We're searching for closest multiple below n, n2 is second candidate
    
    distance_n1 = n - n1
    distance_n2 = n2 - n

    if (distance_n1 == distance_n2):
        # We use key=abs so that max compares values using their absolute values
        return max(n1, n2, key=abs)
    elif (distance_n1 < distance_n2):
        return n1
    else:
        return n2

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