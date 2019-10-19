import unittest
from ParseInputFile import *


class TestParseInputFile(unittest.TestCase):
    def test_hw1_inst1(self):
        self.assertEqual(len(Parse("hw1-inst1.txt")), 10)
        self.assertEqual(Parse("hw1-inst1.txt")[0].GetNumber(), 1)


if __name__ == '__main__':
    unittest.main()
