import unittest
from ParseInputFile import *


class TestParseInputFile(unittest.TestCase):
    def test_hw1_inst1(self):
        people = Parse("../Input_Files/hw1-inst1.txt")
        self.assertEqual(len(people), 10)
        for i in range(0, 10):
            self.assertEqual(people[i].GetNumber(), i+1)

        # Make sure position relationships are correct
        self.assertEqual(people[0].GetAdjLeft(), None)
        self.assertEqual(people[0].GetAdjRight(), people[1])
        self.assertEqual(people[0].GetDown(), people[5])
        self.assertEqual(people[1].GetAdjLeft(), people[0])
        self.assertEqual(people[1].GetAdjRight(), people[2])
        self.assertEqual(people[1].GetDown(), people[6])
        self.assertEqual(people[4].GetAdjLeft(), people[3])
        self.assertEqual(people[4].GetAdjRight(), None)
        self.assertEqual(people[4].GetDown(), people[9])
        self.assertEqual(people[5].GetAdjLeft(), None)
        self.assertEqual(people[5].GetAdjRight(), people[6])
        self.assertEqual(people[5].GetUp(), people[0])
        self.assertEqual(people[6].GetAdjLeft(), people[5])
        self.assertEqual(people[6].GetAdjRight(), people[7])
        self.assertEqual(people[6].GetUp(), people[1])
        self.assertEqual(people[9].GetAdjLeft(), people[8])
        self.assertEqual(people[9].GetAdjRight(), None)
        self.assertEqual(people[9].GetUp(), people[4])

        self.assertEqual(people[0].GetRelationTo(people[1]), -4)
        self.assertEqual(people[0].GetRelationTo(people[9]), -9)
        self.assertEqual(people[9].GetRelationTo(people[0]), -6)
        self.assertEqual(people[9].GetRelationTo(people[8]), 10)

        self.assertEqual(people[0].GetType(), "H")
        self.assertEqual(people[4].GetType(), "H")
        self.assertEqual(people[5].GetType(), "G")
        self.assertEqual(people[9].GetType(), "G")

        self.assertEqual(people[0].GetPosition(), 1)
        self.assertEqual(people[4].GetPosition(), 5)
        self.assertEqual(people[5].GetPosition(), 6)
        self.assertEqual(people[9].GetPosition(), 10)



if __name__ == '__main__':
    unittest.main()
