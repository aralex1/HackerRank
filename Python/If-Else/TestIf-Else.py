import unittest
import sys
from io import StringIO
from If_Else import if_and_else

class IfElseTest(unittest.TestCase):
    def test_if_and_else_odd(self):
        out = StringIO()
        sys.stdout = out
        if_and_else(3)
        self.assertEqual(out.getvalue().strip(), "Weird")

    def test_if_and_else_even_Range2and5(self):
        out = StringIO()
        sys.stdout = out
        if_and_else(2)
        self.assertEqual(out.getvalue().strip(), "Not Weird")

    def test_if_and_else_even_Range6and20(self):
        out = StringIO()
        sys.stdout = out
        if_and_else(8)
        self.assertEqual(out.getvalue().strip(), "Weird")

    def test_if_and_else_even_GreaterThan20(self):
        out = StringIO()
        sys.stdout = out
        if_and_else(22)
        self.assertEqual(out.getvalue().strip(), "Not Weird")

    def test_if_and_else_One(self):
        out = StringIO()
        sys.stdout = out
        if_and_else(1)
        self.assertEqual(out.getvalue().strip(), "Weird")

    def test_if_and_else_odd_Range2and5(self):
        out = StringIO()
        sys.stdout = out
        if_and_else(3)
        self.assertEqual(out.getvalue().strip(), "Weird")

    def test_if_and_else_odd_Range6and20(self):
        out = StringIO()
        sys.stdout = out
        if_and_else(17)
        self.assertEqual(out.getvalue().strip(), "Weird")

    def test_if_and_else_odd_GreaterThan20(self):
        out = StringIO()
        sys.stdout = out
        if_and_else(21)
        self.assertEqual(out.getvalue().strip(), "Weird")



if __name__ == '__main__':
    unittest.main()
