import unittest
# Given a number n, we need to print its table. 
# input:  5 Output:  5 * 1 = 5
# 5 * 2 = 10 # 5 * 3 = 15 # 5 * 4 = 20
# 5 * 5 = 25 # 5 * 6 = 30 # 5 * 7 = 35
# 5 * 8 = 40 # 5 * 9 = 45 # 5 * 10 = 50

def printTable(n, i=1):
    if i == 11:
        return ""
    return f"{n} * {i} = {n * i}\n" + printTable(n, i + 1)

class TestPrintTable(unittest.TestCase):
    def test_positive_number(self):
        expected = "".join(f"5 * {i} = {5 * i}\n" for i in range(1, 11))
        self.assertEqual(printTable(5), expected)

    def test_negative_number(self):
        expected = "".join(f"-3 * {i} = {-3 * i}\n" for i in range(1, 11))
        self.assertEqual(printTable(-3), expected)

    def test_zero(self):
        expected = "".join(f"0 * {i} = 0\n" for i in range(1, 11))
        self.assertEqual(printTable(0), expected)

    def test_base_case(self):
        # Forces the execution of the base case when i reaches 11, 
        # ensuring that the function correctly returns an empty string and terminates the recursion.
        self.assertEqual(printTable(5, 11), "")

if __name__ == "__main__":
    unittest.main()