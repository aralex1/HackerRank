import sys
import unittest
from io import StringIO
from ArithmeticOperators import arithmeticOperators

class IfElseTest(unittest.TestCase):
    def test_1_if_and_else_odd(self):
        out = StringIO()
        sys.stdout = out
        arithmeticOperators(3, 2)
        values = out.getvalue()
        values = values.replace('\n','')
        self.assertEqual(values[0], '5')
        self.assertEqual(values[1], '1')
        self.assertEqual(values[2], '6')

    def test_2_if_and_else_odd(self):
        out = StringIO()
        sys.stdout = out
        arithmeticOperators(8, 0)
        values = out.getvalue()
        values = values.replace('\n','')
        self.assertEqual(values[0], '8')
        self.assertEqual(values[1], '8')
        self.assertEqual(values[2], '0')

        
if __name__ == '__main__':
    unittest.main()
