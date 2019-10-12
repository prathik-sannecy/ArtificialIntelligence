from Error import *

class Person():
    def __init__(self, number, type):
        self.number = number
        self.relations = {}
        self.type = type

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