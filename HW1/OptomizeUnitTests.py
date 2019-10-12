import unittest
import DinnerParty
from Error import *
from Person import *
from Optomize import *


class TestOptomize(unittest.TestCase):
    def test_SwapRegularArray(self):
        table = [[1, 2, 3], [4, 5, 6]]
        table = Swap(table, 0, 1, 1, 2)
        self.assertEqual(table, [[1, 6, 3], [4, 5, 2]])

    def test_SwapDinnerTable(self):
        person1 = Person(0, "G")
        person2 = Person(1, "H")
        person3 = Person(2, "H")
        person4 = Person(3, "H")
        person5 = Person(4, "G")
        person6 = Person(5, "G")
        dinnerTable = [[person1, person2, person3], [person4, person5, person6]]
        dinnerTable = Swap(dinnerTable, 0, 1, 1, 2)
        self.assertEqual(dinnerTable[0][1].GetNumber(), 5)
        self.assertEqual(dinnerTable[1][2].GetNumber(), 1)

if __name__ == '__main__':
    unittest.main()
