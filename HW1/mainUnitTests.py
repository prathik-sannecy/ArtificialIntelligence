import unittest
import DinnerParty
from Error import *


class MyTestCase(unittest.TestCase):
    def testCalcTotalEmpty(self):
        self.assertRaises(BadPartyTableMatrix, DinnerParty.Calc)


if __name__ == '__main__':
    unittest.main()
