import unittest
from Person import *
from Optimize import *
from copy import copy, deepcopy


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

        persons=[person1, person6]

        person1_old = copy(person1)
        person6_old = copy(person6)

        Swap(persons[0], person6)

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

    def test_SwapDinnerTableDoubleSwap(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "H"
        person2 = Person(person_number2, person_type2)
        person_number3 = 3
        person_type3 = "G"
        person3 = Person(person_number3, person_type3)
        person_number4 = 4
        person_type4 = "H"
        person4 = Person(person_number4, person_type4)

        person1.SetDown(person3)
        person2.SetDown(person4)
        person3.SetUp(person1)
        person4.SetUp(person2)

        person1.SetAdjRight(person2)
        person2.SetAdjLeft(person1)
        person3.SetAdjRight(person4)
        person4.SetAdjLeft(person3)








        person1_old = deepcopy(person1)
        person2_old = deepcopy(person2)
        person3_old = deepcopy(person3)
        person4_old = deepcopy(person4)

        Swap(person1, person2)
        Swap(person1, person2)
        Swap(person1, person3)
        Swap(person1, person3)
        Swap(person1, person4)
        Swap(person1, person4)
        Swap(person2, person3)
        Swap(person2, person3)
        Swap(person2, person4)
        Swap(person2, person4)
        Swap(person3, person4)
        Swap(person3, person4)


        person1_new = copy(person1)
        person2_new = copy(person2)
        person3_new = copy(person3)
        person4_new = copy(person4)
        person1 = copy(person1_old)
        person2 = copy(person2_old)
        person3 = copy(person3_old)
        person4 = copy(person4_old)

        self.assertEqual(person1.number, person1_new.number)
        self.assertEqual(person1_new.GetAdjLeft(), person1.GetAdjLeft())
        self.assertEqual(person1_new.GetAdjRight(), person1.GetAdjRight())
        self.assertEqual(person1_new.GetDown(), person1.GetDown())
        self.assertEqual(person1_new.GetUp(), person1.GetUp())
        self.assertEqual(person2.number, person2_new.number)
        self.assertEqual(person2_new.GetAdjLeft(), person2.GetAdjLeft())
        self.assertEqual(person2_new.GetAdjRight(), person2.GetAdjRight())
        self.assertEqual(person2_new.GetDown(), person2.GetDown())
        self.assertEqual(person2_new.GetUp(), person2.GetUp())
        self.assertEqual(person3.number, person3_new.number)
        self.assertEqual(person3_new.GetAdjLeft(), person3.GetAdjLeft())
        self.assertEqual(person3_new.GetAdjRight(), person3.GetAdjRight())
        self.assertEqual(person3_new.GetDown(), person3.GetDown())
        self.assertEqual(person3_new.GetUp(), person3.GetUp())
        self.assertEqual(person4.number, person4_new.number)
        self.assertEqual(person4_new.GetAdjLeft(), person4.GetAdjLeft())
        self.assertEqual(person4_new.GetAdjRight(), person4.GetAdjRight())
        self.assertEqual(person4_new.GetDown(), person4.GetDown())
        self.assertEqual(person4_new.GetUp(), person4.GetUp())
        


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

    def test_OptimizeTwoByTwo(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "H"
        person2 = Person(person_number2, person_type2)
        person_number3 = 3
        person_type3 = "G"
        person3 = Person(person_number3, person_type3)
        person_number4 = 4
        person_type4 = "H"
        person4 = Person(person_number4, person_type4)

        person1.SetDown(person3)
        person2.SetDown(person4)
        person3.SetUp(person1)
        person4.SetUp(person2)

        person1.SetAdjRight(person2)
        person2.SetAdjLeft(person1)
        person3.SetAdjRight(person4)
        person4.SetAdjLeft(person3)

        person1.SetRelationTo(person2, 1)
        person1.SetRelationTo(person3, 2)
        person1.SetRelationTo(person4, 3)
        person2.SetRelationTo(person1, 4)
        person2.SetRelationTo(person3, 5)
        person2.SetRelationTo(person4, 6)
        person3.SetRelationTo(person1, 7)
        person3.SetRelationTo(person2, 8)
        person3.SetRelationTo(person4, 9)
        person4.SetRelationTo(person1, 10)
        person4.SetRelationTo(person2, 11)
        person4.SetRelationTo(person3, 12)

        dinnerTable = [person1, person2, person3, person4]

        score, people = Optimize(dinnerTable, 0, 1, float("-inf"))
        print(score)

    def test_OptimizeThreeByTwo(self):
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

        person1.SetRelationTo(person2, -1)
        person1.SetRelationTo(person3, -5)
        person1.SetRelationTo(person4, 0)
        person1.SetRelationTo(person5, -9)
        person1.SetRelationTo(person6, -5)
        person2.SetRelationTo(person1, -8)
        person2.SetRelationTo(person3, -5)
        person2.SetRelationTo(person4, -7)
        person2.SetRelationTo(person5, -4)
        person2.SetRelationTo(person6, 9)
        person3.SetRelationTo(person1, 1)
        person3.SetRelationTo(person2, -2)
        person3.SetRelationTo(person4, 7)
        person3.SetRelationTo(person5, 8)
        person3.SetRelationTo(person6, 1)
        person4.SetRelationTo(person1, 2)
        person4.SetRelationTo(person2, 2)
        person4.SetRelationTo(person3, 7)
        person4.SetRelationTo(person5, 1)
        person4.SetRelationTo(person6, 0)
        person5.SetRelationTo(person1, 10)
        person5.SetRelationTo(person2, 6)
        person5.SetRelationTo(person3, -6)
        person5.SetRelationTo(person4, 0)
        person5.SetRelationTo(person6, 6)
        person6.SetRelationTo(person1, -8)
        person6.SetRelationTo(person2, -7)
        person6.SetRelationTo(person3, -6)
        person6.SetRelationTo(person4, -6)
        person6.SetRelationTo(person5, 7)

        dinnerTable = [person1, person2, person3, person4, person5, person6]

        print(Optimize(dinnerTable, 0, 1, float("-inf")))

if __name__ == '__main__':
    unittest.main()
