import unittest
import DinnerParty
from Error import *
from Person import *


class TestDinnerParty(unittest.TestCase):
    def test_CalcTotalEmpty(self):
        self.assertRaises(BadPartyTableMatrix, DinnerParty.Calc, [])

    def test_CalcTotalTwoByOne(self):
        person1 = Person(0, "G")
        person2 = Person(1, "H")
        person1.SetRelationTo(person2.GetNumber(), "4")
        person2.SetRelationTo(person1.GetNumber(), "2")
        dinnerTable = [[person1], [person2]]
        self.assertEqual(DinnerParty.Calc(dinnerTable), 8)

    def test_CalcTotalTwoByThree(self):
        person1 = Person(0, "G")
        person2 = Person(1, "H")
        person3 = Person(2, "H")
        person4 = Person(3, "H")
        person5 = Person(4, "G")
        person6 = Person(5, "G")
        person1.SetRelationTo(person2.GetNumber(), 2)
        person2.SetRelationTo(person1.GetNumber(), 3)
        person2.SetRelationTo(person3.GetNumber(), 0)
        person3.SetRelationTo(person2.GetNumber(), 1)
        person4.SetRelationTo(person5.GetNumber(), -1)
        person5.SetRelationTo(person4.GetNumber(), -2)
        person5.SetRelationTo(person6.GetNumber(), 2)
        person6.SetRelationTo(person5.GetNumber(), 0)

        person1.SetRelationTo(person4.GetNumber(), 2)
        person4.SetRelationTo(person1.GetNumber(), 3)
        person2.SetRelationTo(person5.GetNumber(), -1)
        person5.SetRelationTo(person2.GetNumber(), 1)
        person3.SetRelationTo(person6.GetNumber(), 2)
        person6.SetRelationTo(person3.GetNumber(), 1)

        dinnerTable = [[person1, person2, person3], [person4, person5, person6]]
        self.assertEqual(DinnerParty.Calc(dinnerTable), 21)

    def test_CalcRowTest1(self):
        person1 = Person(0, "G")
        person2 = Person(1, "H")
        person3 = Person(2, "G")
        person4 = Person(3, "H")
        person1.SetRelationTo(person2.GetNumber(), 2)
        person2.SetRelationTo(person1.GetNumber(), 3)
        person2.SetRelationTo(person3.GetNumber(), 0)
        person3.SetRelationTo(person2.GetNumber(), 1)
        person3.SetRelationTo(person4.GetNumber(), -1)
        person4.SetRelationTo(person3.GetNumber(), -2)
        tableRow = [person1, person2, person3, person4]
        self.assertEqual(DinnerParty.CalcAdjHostGuest(tableRow), 6)

    def test_CalcRowTest2(self):
        person1 = Person(0, "G")
        person2 = Person(1, "H")
        person3 = Person(2, "H")
        person4 = Person(3, "G")
        person1.SetRelationTo(person2.GetNumber(), 2)
        person2.SetRelationTo(person1.GetNumber(), 3)
        person2.SetRelationTo(person3.GetNumber(), 0)
        person3.SetRelationTo(person2.GetNumber(), 1)
        person3.SetRelationTo(person4.GetNumber(), -1)
        person4.SetRelationTo(person3.GetNumber(), -2)
        tableRow = [person1, person2, person3, person4]
        self.assertEqual(DinnerParty.CalcAdjHostGuest(tableRow), 5)


    def test_CalcColumnTest1(self):
        person1 = Person(0, "G")
        person2 = Person(1, "H")
        person3 = Person(2, "G")
        person4 = Person(3, "H")
        person1.SetRelationTo(person3.GetNumber(), 2)
        person3.SetRelationTo(person1.GetNumber(), 3)
        person2.SetRelationTo(person4.GetNumber(), -1)
        person4.SetRelationTo(person2.GetNumber(), 1)
        dinnerTable = [[person1, person2], [person3, person4]]
        self.assertEqual(DinnerParty.CalcOppHostGuest(dinnerTable), 5)

    def test_CalcColumnTest2(self):
        person1 = Person(0, "G")
        person2 = Person(1, "H")
        person3 = Person(2, "H")
        person4 = Person(3, "G")
        person1.SetRelationTo(person3.GetNumber(), 2)
        person3.SetRelationTo(person1.GetNumber(), 3)
        person2.SetRelationTo(person4.GetNumber(), -1)
        person4.SetRelationTo(person2.GetNumber(), 1)
        dinnerTable = [[person1, person2], [person3, person4]]
        self.assertEqual(DinnerParty.CalcOppHostGuest(dinnerTable), 9)




if __name__ == '__main__':
    unittest.main()
