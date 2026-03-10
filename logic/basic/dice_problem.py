import unittest

# You are given a cubic dice with 6 faces. 
# All the individual faces have a number printed on them. 
# The numbers are in the range of 1 to 6, like any ordinary dice. 
# You will be provided with a face of this cube, 
# your task is to guess the number on the opposite face of the cube.

def guess_opposite_face(face):
    if face == 1:
        return 6
    if face == 2:
        return 5
    if face == 3:
        return 4
    if face == 4:
        return 3
    if face == 5:
        return 2
    if face == 6:
        return 1
    
def guess_opposite_with_sum(face):
    # If you notice, the sum of all opposite faces is always 7.
    # So, we can simply subtract to have the value.
    return 7 - face

class TestDiceProblem(unittest.TestCase):
    def test_guess_opposite_face(self):
        self.assertEqual(guess_opposite_face(1), 6)
        self.assertEqual(guess_opposite_face(2), 5)
        self.assertEqual(guess_opposite_face(3), 4)
        self.assertEqual(guess_opposite_face(4), 3)
        self.assertEqual(guess_opposite_face(5), 2)
        self.assertEqual(guess_opposite_face(6), 1)

    def test_guess_opposite_with_sum(self):
        self.assertEqual(guess_opposite_with_sum(1), 6)
        self.assertEqual(guess_opposite_with_sum(2), 5)
        self.assertEqual(guess_opposite_with_sum(3), 4)
        self.assertEqual(guess_opposite_with_sum(4), 3)
        self.assertEqual(guess_opposite_with_sum(5), 2)
        self.assertEqual(guess_opposite_with_sum(6), 1)

if __name__ == '__main__':
    unittest.main()