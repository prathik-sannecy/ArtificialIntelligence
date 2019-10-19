import unittest
from DinnerTableMain import *


class DinnerTableMainUnitTests(unittest.TestCase):
    def test_GetArrangementsInst1(self):
        Main("Input_Files/hw1-inst1.txt")


    def test_GetArrangementsInst2(self):
        Main("Input_Files/hw1-inst2.txt")


    def test_GetArrangementsInst3(self):
        Main("Input_Files/hw1-inst3.txt")


if __name__ == '__main__':
    unittest.main()
