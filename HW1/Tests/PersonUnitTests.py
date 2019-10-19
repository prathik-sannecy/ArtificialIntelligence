import unittest
from Person import *


class TestPerson(unittest.TestCase):
    def test_CreatePerson(self):
        person_number = 1
        person1 = Person(person_number, "G")
        self.assertEqual(person1.number, person_number)

    def test_AddRelationToSelfError(self):
        person_number = 1
        person1 = Person(person_number, "G")
        self.assertRaises(InvalidPersonOperation, person1.SetRelationTo, person1, 10)

    def test_AddRelationToOther(self):
        person1_number = 1
        person2_number = 2
        person1 = Person(person1_number, "G")
        person2 = Person(person2_number, "G")
        person1.SetRelationTo(person2, 10)
        self.assertEqual(person1.relations[person2], 10)

    def test_GetRelationToOther(self):
        person1_number = 1
        person2_number = 2
        person2_relation = 10
        person1 = Person(person1_number, "G")
        person2 = Person(person2_number, "G")
        person1.SetRelationTo(person2, person2_relation)
        self.assertEqual(person1.GetRelationTo(person2), person2_relation)

    def test_GetRelationToSelfError(self):
        person1_number = 1
        person1 = Person(person1_number, "G")
        self.assertRaises(InvalidPersonOperation, person1.GetRelationTo, person1)

    def test_GetRelationToUnknownPersonError(self):
        person1_number = 1
        person2_number = 2
        person1 = Person(person1_number, "G")
        person2 = Person(person2_number, "G")
        self.assertRaises(InvalidPersonOperation, person1.GetRelationTo, person2)

    def test_GetNumber(self):
        person_number = 1
        person = Person(person_number, "G")
        self.assertEqual(person.GetNumber(), person_number)

    def test_GetType(self):
        person_number = 1
        person_type = "G"
        person = Person(person_number, person_type)
        self.assertEqual(person.GetType(), person_type)

    def test_AddAdjLeft(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "G"
        person2 = Person(person_number2, person_type2)
        person1.SetAdjLeft(person2)
        self.assertEqual(person1.GetAdjLeft(), person2)

    def test_AddAdjRight(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "G"
        person2 = Person(person_number2, person_type2)
        person1.SetAdjRight(person2)
        self.assertEqual(person1.GetAdjRight(), person2)

    def test_AddDown(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "G"
        person2 = Person(person_number2, person_type2)
        person1.SetDown(person2)
        self.assertEqual(person1.GetDown(), person2)

    def test_AddUp(self):
        person_number1 = 1
        person_type1 = "G"
        person1 = Person(person_number1, person_type1)
        person_number2 = 2
        person_type2 = "G"
        person2 = Person(person_number2, person_type2)
        person1.SetUp(person2)
        self.assertEqual(person1.GetUp(), person2)

    def test_Score(self):
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

        self.assertEqual(person1.GetScore(), 7)
        self.assertEqual(person2.GetScore(), 5)
        self.assertEqual(person3.GetScore(), 5)
        self.assertEqual(person4.GetScore(), 5)
        self.assertEqual(person5.GetScore(), 4)
        self.assertEqual(person6.GetScore(), 3)




if __name__ == '__main__':
    unittest.main()
