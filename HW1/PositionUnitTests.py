import unittest
import DinnerParty
from Error import *
from Person import *
from Position import *

class TestPerson(unittest.TestCase):
    def test_Position(self):
        x = 5
        y = 10
        position = Position()
        position.SetPos(x, y)
        self.assertEqual(position.GetPos(), (x, y))