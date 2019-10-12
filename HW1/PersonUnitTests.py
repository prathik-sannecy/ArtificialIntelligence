import unittest
import DinnerParty
from Error import *
from Person import *


class TestPerson(unittest.TestCase):
    def test_CreatePerson(self):
        person_number = 1
        person1 = Person(person_number, "G")
        self.assertEqual(person1.number, person_number)

    def test_AddRelationToSelfError(self):
        person_number = 1
        person1 = Person(person_number, "G")
        self.assertRaises(InvalidPersonOperation, person1.SetRelationTo, person_number, 10)

    def test_AddRelationToOther(self):
        person1_number = 1
        person2_number = 2
        person1 = Person(person1_number, "G")
        person1.SetRelationTo(person2_number, 10)
        self.assertEqual(person1.relations[person2_number], 10)

    def test_GetRelationToOther(self):
        person1_number = 1
        person2_number = 2
        person2_relation = 10
        person1 = Person(person1_number, "G")
        person1.SetRelationTo(person2_number, person2_relation)
        self.assertEqual(person1.GetRelationTo(person2_number), person2_relation)

    def test_GetRelationToSelfError(self):
        person1_number = 1
        person1 = Person(person1_number, "G")
        self.assertRaises(InvalidPersonOperation, person1.GetRelationTo, person1_number)

    def test_GetRelationToUnknownPersonError(self):
        person1_number = 1
        person2_number = 2
        person1 = Person(person1_number, "G")
        self.assertRaises(InvalidPersonOperation, person1.GetRelationTo, person2_number)

    def test_GetNumber(self):
        person_number = 1
        person = Person(person_number, "G")
        self.assertEqual(person.GetNumber(), person_number)

    def test_GetType(self):
        person_number = 1
        person_type = "G"
        person = Person(person_number, person_type)
        self.assertEqual(person.GetType(), person_type)



if __name__ == '__main__':
    unittest.main()
