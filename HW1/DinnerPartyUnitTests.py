import unittest
import DinnerParty
from Error import *
from Person import *


class TestDinnerParty(unittest.TestCase):
    def testCalcTotalEmpty(self):
        self.assertRaises(BadPartyTableMatrix, DinnerParty.Calc)




if __name__ == '__main__':
    unittest.main()
