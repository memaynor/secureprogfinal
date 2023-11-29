import mod6project
import unittest
from io import StringIO
import sys

class Tests(unittest.TestCase):
    def setUp(self):
        self.originalOut = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.originalOut

    def testEncryptWork(self):
        input_string = "testing"
        expected_result = "116.100.113.116.101.105.97"

        with unittest.mock.patch('builtins.input', side_effect=[input_string]):
            mod6project.encrypt()
            result = sys.stdout.getvalue().strip()

        self.assertEqual(result, expected_result)
if __name__ == "__main__":
    unittest.main()