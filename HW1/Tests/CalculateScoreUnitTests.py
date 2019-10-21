import unittest
import CalculateScore
from Person import *


class TestDinnerParty(unittest.TestCase):
    def test_CalcTotalTwoByThree(self):
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

        person1.SetRelationTo(person2, 2)
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

        dinnerTable = {person1, person2, person3, person4, person5, person6}

        self.assertEqual(CalculateScore.Calc(dinnerTable), 29)





if __name__ == '__main__':
    unittest.main()
