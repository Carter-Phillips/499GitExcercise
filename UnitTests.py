import GitExcercise
import unittest

class UnitTests(unittest.TestCase):
    def test_Cross(self):
        cross = 'x    x\n x  x \n  xx  \n  xx  \n x  x \nx    x\n'
        self.assertEqual(GitExcercise.cross(), cross)

    def test_Triangle(self):
        triangle = '\n             /\\\n            /  \\\n           /    \\\n          /______\\\n          '
        self.assertEqual(GitExcercise.triangle(), triangle)

    def test_Square(self):
        square = ' ________\n|        |\n|        |\n|        |\n|        |\n|        |\n ‾‾‾‾‾‾‾‾'
        self.assertEqual(GitExcercise.square(), square)

if __name__ == '__main__':
    unittest.main()