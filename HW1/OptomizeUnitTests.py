import unittest
import DinnerParty
from Error import *
from Person import *
from Optomize import *
from copy import copy, copy


class TestOptomize(unittest.TestCase):
    def test_SwapDinnerTableLeftEdge(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "H"
        person2 = Person(person_number2, person_type2)
        person_number3 = 3
        person_type3 = "H"
        person3 = Person(person_number3, person_type3)
        person_number4 = 4
        person_type4 = "H"
        person4 = Person(person_number4, person_type4)
        person_number5 = 5
        person_type5 = "G"
        person5 = Person(person_number5, person_type5)
        person_number6 = 6
        person_type6 = "G"
        person6 = Person(person_number6, person_type6)

        person1.SetDown(person4)
        person2.SetDown(person5)
        person3.SetDown(person6)
        person4.SetUp(person1)
        person5.SetUp(person2)
        person6.SetUp(person3)

        person1.SetAdjRight(person2)
        person2.SetAdjLeft(person1)
        person2.SetAdjRight(person3)
        person3.SetAdjLeft(person2)
        person4.SetAdjRight(person5)
        person5.SetAdjLeft(person4)
        person5.SetAdjRight(person6)
        person6.SetAdjLeft(person5)

        person1.SetRelationTo(person2, 8)
        person2.SetRelationTo(person1, 3)
        person2.SetRelationTo(person3, 0)
        person3.SetRelationTo(person2, 1)
        person4.SetRelationTo(person5, -1)
        person5.SetRelationTo(person4, -2)
        person5.SetRelationTo(person6, 2)
        person6.SetRelationTo(person5, 0)

        person1.SetRelationTo(person4, 2)
        person4.SetRelationTo(person1, 3)
        person2.SetRelationTo(person5, -1)
        person5.SetRelationTo(person2, 1)
        person3.SetRelationTo(person6, 2)
        person6.SetRelationTo(person3, 1)


        person1_old = copy(person1)
        person4_old = copy(person4)

        Swap(person1, person4)

        person1_new = copy(person1)
        person4_new = copy(person4)
        person1 = copy(person1_old)
        person4 = copy(person4_old)

        self.assertEqual(person1.number, person1_new.number)
        self.assertEqual(person1.GetRelationTo(person4), person1_new.GetRelationTo(person4))
        self.assertEqual(person1_new.GetAdjLeft(), person4.GetAdjLeft())
        self.assertEqual(person1_new.GetAdjRight(), person4.GetAdjRight())
        self.assertEqual(person1_new.GetDown(), None)
        self.assertEqual(person1_new.GetUp(), person4)
        self.assertEqual(person4.number, person4_new.number)
        self.assertEqual(person4.GetRelationTo(person1), person4_new.GetRelationTo(person1))
        self.assertEqual(person4_new.GetAdjLeft(), person1.GetAdjLeft())
        self.assertEqual(person4_new.GetAdjRight(), person1.GetAdjRight())
        self.assertEqual(person4_new.GetDown(), person1)
        self.assertEqual(person4_new.GetUp(), None)

    def test_SwapDinnerTableMiddle(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "H"
        person2 = Person(person_number2, person_type2)
        person_number3 = 3
        person_type3 = "H"
        person3 = Person(person_number3, person_type3)
        person_number4 = 4
        person_type4 = "H"
        person4 = Person(person_number4, person_type4)
        person_number5 = 5
        person_type5 = "G"
        person5 = Person(person_number5, person_type5)
        person_number6 = 6
        person_type6 = "G"
        person6 = Person(person_number6, person_type6)

        person1.SetDown(person4)
        person2.SetDown(person5)
        person3.SetDown(person6)
        person4.SetUp(person1)
        person5.SetUp(person2)
        person6.SetUp(person3)

        person1.SetAdjRight(person2)
        person2.SetAdjLeft(person1)
        person2.SetAdjRight(person3)
        person3.SetAdjLeft(person2)
        person4.SetAdjRight(person5)
        person5.SetAdjLeft(person4)
        person5.SetAdjRight(person6)
        person6.SetAdjLeft(person5)




        person1_old = copy(person1)
        person5_old = copy(person5)

        Swap(person1, person5)

        person1_new = copy(person1)
        person5_new = copy(person5)
        person1 = copy(person1_old)
        person5 = copy(person5_old)

        self.assertEqual(person1.number, person1_new.number)
        self.assertEqual(person1_new.GetAdjLeft(), person5.GetAdjLeft())
        self.assertEqual(person1_new.GetAdjRight(), person5.GetAdjRight())
        self.assertEqual(person1_new.GetDown(), person5.GetDown())
        self.assertEqual(person1_new.GetUp(), person5.GetUp())
        self.assertEqual(person5.number, person5_new.number)
        self.assertEqual(person5_new.GetAdjLeft(), person1.GetAdjLeft())
        self.assertEqual(person5_new.GetAdjRight(), person1.GetAdjRight())
        self.assertEqual(person5_new.GetDown(), person1.GetDown())
        self.assertEqual(person5_new.GetUp(), person1.GetUp())

    def test_SwapDinnerTableRight(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "H"
        person2 = Person(person_number2, person_type2)
        person_number3 = 3
        person_type3 = "H"
        person3 = Person(person_number3, person_type3)
        person_number4 = 4
        person_type4 = "H"
        person4 = Person(person_number4, person_type4)
        person_number5 = 5
        person_type5 = "G"
        person5 = Person(person_number5, person_type5)
        person_number6 = 6
        person_type6 = "G"
        person6 = Person(person_number6, person_type6)

        person1.SetDown(person4)
        person2.SetDown(person5)
        person3.SetDown(person6)
        person4.SetUp(person1)
        person5.SetUp(person2)
        person6.SetUp(person3)

        person1.SetAdjRight(person2)
        person2.SetAdjLeft(person1)
        person2.SetAdjRight(person3)
        person3.SetAdjLeft(person2)
        person4.SetAdjRight(person5)
        person5.SetAdjLeft(person4)
        person5.SetAdjRight(person6)
        person6.SetAdjLeft(person5)

        person1.SetRelationTo(person2, 8)
        person2.SetRelationTo(person1, 3)
        person2.SetRelationTo(person3, 0)
        person3.SetRelationTo(person2, 1)
        person4.SetRelationTo(person5, -1)
        person5.SetRelationTo(person4, -2)
        person5.SetRelationTo(person6, 2)
        person6.SetRelationTo(person5, 0)

        person1.SetRelationTo(person4, 2)
        person4.SetRelationTo(person1, 3)
        person2.SetRelationTo(person5, -1)
        person5.SetRelationTo(person2, 1)
        person3.SetRelationTo(person6, 2)
        person6.SetRelationTo(person3, 1)


        person1_old = copy(person1)
        person6_old = copy(person6)

        Swap(person1, person6)

        person1_new = copy(person1)
        person6_new = copy(person6)
        person1 = copy(person1_old)
        person6 = copy(person6_old)

        self.assertEqual(person1.number, person1_new.number)
        self.assertEqual(person1_new.GetAdjLeft(), person6.GetAdjLeft())
        self.assertEqual(person1_new.GetAdjRight(), person6.GetAdjRight())
        self.assertEqual(person1_new.GetDown(), person6.GetDown())
        self.assertEqual(person1_new.GetUp(), person6.GetUp())
        self.assertEqual(person6.number, person6_new.number)
        self.assertEqual(person6_new.GetAdjLeft(), person1.GetAdjLeft())
        self.assertEqual(person6_new.GetAdjRight(), person1.GetAdjRight())
        self.assertEqual(person6_new.GetDown(), person1.GetDown())
        self.assertEqual(person6_new.GetUp(), person1.GetUp())


    def test_SwapDinnerTableRelationsPreserved(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "H"
        person2 = Person(person_number2, person_type2)
        person_number3 = 3
        person_type3 = "H"
        person3 = Person(person_number3, person_type3)
        person_number4 = 4
        person_type4 = "H"
        person4 = Person(person_number4, person_type4)
        person_number5 = 5
        person_type5 = "G"
        person5 = Person(person_number5, person_type5)
        person_number6 = 6
        person_type6 = "G"
        person6 = Person(person_number6, person_type6)

        person1.SetDown(person4)
        person2.SetDown(person5)
        person3.SetDown(person6)
        person4.SetUp(person1)
        person5.SetUp(person2)
        person6.SetUp(person3)

        person1.SetAdjRight(person2)
        person2.SetAdjLeft(person1)
        person2.SetAdjRight(person3)
        person3.SetAdjLeft(person2)
        person4.SetAdjRight(person5)
        person5.SetAdjLeft(person4)
        person5.SetAdjRight(person6)
        person6.SetAdjLeft(person5)

        person1.SetRelationTo(person2, 8)
        person2.SetRelationTo(person1, 3)
        person2.SetRelationTo(person3, 0)
        person3.SetRelationTo(person2, 1)
        person4.SetRelationTo(person5, -1)
        person5.SetRelationTo(person4, -2)
        person5.SetRelationTo(person6, 2)
        person6.SetRelationTo(person5, 0)

        person1.SetRelationTo(person4, 2)
        person4.SetRelationTo(person1, 3)
        person2.SetRelationTo(person5, -1)
        person5.SetRelationTo(person2, 1)
        person3.SetRelationTo(person6, 2)
        person6.SetRelationTo(person3, 1)

        Swap(person1, person6)

        self.assertEqual(person1.GetRelationTo(person2), 8)
        self.assertEqual(person1.GetAdjLeft(), person5)

if __name__ == '__main__':
    unittest.main()
