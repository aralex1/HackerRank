import unittest
import sys
from io import StringIO
import HelloWorld

class TestHelloWorld(unittest.TestCase):

    def test_TestHelloWorld(self):
        out = StringIO()
        sys.stdout = out
        HelloWorld.HelloWorld()
        self.assertEqual(out.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    
    unittest.main(verbosity = 2)
