import unittest
# Given a number n, we need to print its table. 
# input:  5 Output:  5 * 1 = 5
# 5 * 2 = 10 # 5 * 3 = 15 # 5 * 4 = 20
# 5 * 5 = 25 # 5 * 6 = 30 # 5 * 7 = 35
# 5 * 8 = 40 # 5 * 9 = 45 # 5 * 10 = 50

def print_multiplication_table(n):
    result = ""
    for i in range(1, 11):
        # If we print a string, the output to the terminal is 'None' which leads to failure of the test cases.  
        # So we need to return the string instead of printing it.
        result += f"{n} x {i} = {n * i}\n"
    return result


class TestPrintMultiplicationTable(unittest.TestCase):
    # Test cases for the function print_multiplication_table
    def test_positive_number(self):
        expected = "".join(f"5 x {i} = {5 * i}\n" for i in range(1, 11))
        self.assertEqual(print_multiplication_table(5), expected)
    
    def test_negative_number(self):
        expected = "".join(f"-3 x {i} = {-3 * i}\n" for i in range(1, 11))
        self.assertEqual(print_multiplication_table(-3), expected)
    
    def test_zero(self):
        expected = "".join(f"0 x {i} = 0\n" for i in range(1, 11))
        self.assertEqual(print_multiplication_table(0), expected) 

if __name__ == "__main__":
    unittest.main()