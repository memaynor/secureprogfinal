import mod6project
import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch

class Tests(unittest.TestCase):
    def setUp(self):
        self.originalOut = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.originalOut

    def testEncryptWork(self):
        originalText = "textfile.txt"
        outputFile = "outputForTest.txt"
        files = [originalText, outputFile]
        expectedResult = "116.100.113.116.101.105.97"

        with patch('builtins.input', side_effect=files):
            mod6project.encrypt()

        with open(outputFile, "r") as output:
            result = output.read().strip()

        os.remove(outputFile)

        self.assertEqual(result, expectedResult)

    def testEncryptFileNotFound(self):
        originalText = "notrealfile"
        outputFile = "outputForTest.txt"
        files = [originalText, outputFile]
        expectedResult = "Input file not found, try again."

        with patch('builtins.input', side_effect=files):
            mod6project.encrypt()
            result = sys.stdout.getvalue().strip()

        self.assertEqual(result, expectedResult)
    
    def testDecryptWork(self):
        originalText = "encrypted.txt"
        outputFile = "outputForTest.txt"
        files = [originalText, outputFile]
        expectedResult = "testing"

        with patch('builtins.input', side_effect=files):
            mod6project.decrypt()

        with open(outputFile, "r") as output:
            result = output.read().strip()

        os.remove(outputFile)

        self.assertEqual(result, expectedResult)
    def testDecryptFileNotFound(self):
        originalText = "notrealfile"
        outputFile = "outputForTest.txt"
        files = [originalText, outputFile]
        expectedResult = "Input file not found, try again."

        with patch('builtins.input', side_effect=files):
            mod6project.decrypt()
            result = sys.stdout.getvalue().strip()

        self.assertEqual(result, expectedResult)

    def testDecryptAlready(self):
        originalText = "textfile.txt"
        outputFile = "outputForTest.txt"
        files = [originalText, outputFile]
        expectedResult = "File is not encrypted, try again"

        with patch('builtins.input', side_effect=files):
            mod6project.decrypt()
            result = sys.stdout.getvalue().strip()

        self.assertEqual(result, expectedResult)

if __name__ == "__main__":
    unittest.main()