from Error import *
from Position import *

class Person():
    def __init__(self, number, type):
        self.number = number
        self.relations = {}
        self.type = type
        self.adjRight = None
        self.adjLeft = None
        self.down = None
        self.up = None


    def SetRelationTo(self, person, value):
        if person == self.number:
            raise InvalidPersonOperation("Can't set relation to self")
        self.relations[person] = value

    def GetRelationTo(self, person):
        if person == self.number:
            raise InvalidPersonOperation("Can't get relation to self")
        if person in self.relations.keys():
            return self.relations[person]
        else:
            raise InvalidPersonOperation("Relation from " + str(self.number) + " to " + str(person) + " not found")

    def GetNumber(self):
        return self.number

    def GetType(self):
        return self.type

    def SetPosition(self, position):
        self.position = position

    def GetPosition(self):
        return self.position

    def SetAdjRight(self, person):
        self.adjRight = person

    def GetAdjRight(self):
        return self.adjRight

    def SetAdjLeft(self, person):
        self.adjLeft = person

    def GetAdjLeft(self):
        return self.adjLeft

    def SetDown(self, person):
        self.down = person

    def GetDown(self):
        return self.down

    def SetUp(self, person):
        self.up = person

    def GetUp(self):
        return self.up

    def GetScore(self):
        score = 0
        if self.adjRight:
            if self.adjRight.GetType() != self.GetType():
                score += 1
            score += self.GetRelationTo(self.adjRight)
        if self.down:
            if self.down.GetType() != self.GetType():
                score += 2
            score += self.GetRelationTo(self.down)
        if self.adjLeft:
            score += self.GetRelationTo(self.adjLeft)
        if self.up:
            score += self.GetRelationTo(self.up)

        return score