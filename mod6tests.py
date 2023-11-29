import mod6project
import unittest
from unittest.mock import patch

class Tests(unittest.TestCase):

    def testEncryptWork(self):
        files = ["textfile.txt", "encrypted.txt"]
        expectedResult = "116.100.113.116.101.105.97"

        with patch('builtins.input', side_effect=files):
            mod6project.encrypt()

        with open("encrypted.txt", "r") as output:
            result = output.read().strip()

        self.assertEqual(result, expectedResult)

if __name__ == "__main__":
    unittest.main()