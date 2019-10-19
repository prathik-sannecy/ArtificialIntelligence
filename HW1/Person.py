from Error import *
from Position import *


class Person():
    """A person sitting at the dinner table"""
    def __init__(self, number, type):
        self.number = number
        self.relations = {}
        self.type = type
        self.adjRight = None
        self.adjLeft = None
        self.down = None
        self.up = None
        self.position = 0

    def __eq__(self, other):
        """Each person has a unique id"""
        if other is None: return True
        return self.number == other.number

    def __hash__(self):
        """Each person has a unique id"""
        return hash((self.number))

    def SetRelationTo(self, person, value):
        """Set the relationship to another person

        inputs:
            (person) the person to set the relationship to
            (int) the value of the relationship to that person
        returns:
            None
        """
        assert (type(person) == Person or person is None)
        if person == self and person is not None:
            raise InvalidPersonOperation("Can't set relation to self")
        self.relations[person] = value

    def GetRelationTo(self, person):
        """Gets the relation to another person based on relationship list

        inputs:
            (person) the person to get the relationship to
        returns:
            None
        """
        assert (type(person) == Person or person is None)
        if person == self and person is not None:
            raise InvalidPersonOperation("Can't get relation to self")
        if person in self.relations.keys():
            return self.relations[person]
        else:
            raise InvalidPersonOperation("Relation from " + str(self.number) + " to " + str(person.number) + " not found")

    def GetNumber(self):
        """Returns unique person's identification number

        inputs:
            None
        returns:
            (int) the unique of of the person
        """
        return self.number

    def GetType(self):
        """Returns 'G' if Guest, 'H' if Host

        inputs:
            None
        returns:
            (string) 'G' if Guest, 'H' if Host
        """
        return self.type

    def SetPosition(self, position):
        """Set the position of the person

        inputs:
            (int) the table position of the person
        returns:
            None
        """
        self.position = position

    def GetPosition(self):
        """Gets the position of the person at the table
        inputs:
            None
        returns:
            (int) the table position of the person
        """
        return self.position

    def SetAdjRight(self, person):
        """Sets the person to the right of this person

        inputs:
            (Person) the person to the right of this person
        returns:
            None
        """
        assert (type(person) == Person or person is None)
        if person == self and person is not None:
            raise InvalidPersonOperation("Can't be adjacent to self")
        self.adjRight = person

    def GetAdjRight(self):
        """Gets the person to the right of this person

        inputs:
            None
        returns:
            (Person) the person to the right of this person
        """
        return self.adjRight

    def SetAdjLeft(self, person):
        """Sets the person to the left of this person

        inputs:
            (Person) the person to the left of this person
        returns:
            None
        """
        assert (type(person) == Person or person is None)
        if person == self and person is not None:
            raise InvalidPersonOperation("Can't be adjacent to self")
        self.adjLeft = person

    def GetAdjLeft(self):
        """Gets the person to the left of this person

        inputs:
            None
        returns:
            (Person) the person to the left of this person
        """
        return self.adjLeft

    def SetDown(self, person):
        """Sets the person below (looking topdown at the table) of this person

        inputs:
            (Person) the person below this person
        returns:
            None
        """
        assert (type(person) == Person or person is None)
        if person == self and person is not None:
            raise InvalidPersonOperation("Can't be opposite to self")
        self.down = person

    def GetDown(self):
        """Gets the person below (looking topdown at the table) of this person

        inputs:
            None
        returns:
            (Person) the person below this person
        """
        return self.down

    def SetUp(self, person):
        """Sets the person above (looking topdown at the table) of this person

        inputs:
            (Person) the person above this person
        returns:
            None
        """
        assert (type(person) == Person or person is None)
        if person == self and person is not None:
            raise InvalidPersonOperation("Can't be opposite to self")
        self.up = person

    def GetUp(self):
        """Gets the person above (looking topdown at the table) of this person

        inputs:
            None
        returns:
            (Person) the person above this person
        """
        return self.up

    def GetScore(self):
        """Returns the total score for this particular person

        inputs:
            None
        returns:
            (int) the score of this particular person
        """
        score = 0
        # If there is a person to the right of this person...
        if self.adjRight:
            # Increment the score by 1 if the person is of opposite type (guest to host and vice/versa)
            if self.adjRight.GetType() != self.GetType():
                score += 1
            # Increment the score by the person's relationship to this person
            score += self.GetRelationTo(self.adjRight)
        # If there is a person below (looking topdown) of this person...
        if self.down:
            # Increment the score by 2 if the person is of opposite type (guest to host and vice/versa)
            if self.down.GetType() != self.GetType():
                score += 2
            # Increment the score by the person's relationship to this person
            score += self.GetRelationTo(self.down)
        # If there is a person to the left of this person...
        if self.adjLeft:
            # Increment the score by 1 if the person is of opposite type (guest to host and vice/versa)
            if self.adjLeft.GetType() != self.GetType():
                score += 1
            # Increment the score by the person's relationship to this person
            score += self.GetRelationTo(self.adjLeft)
        # If there is a person above (looking topdown) of this person...
        if self.up:
            # Increment the score by 2 if the person is of opposite type (guest to host and vice/versa)
            if self.up.GetType() != self.GetType():
                score += 2
            # Increment the score by the person's relationship to this person
            score += self.GetRelationTo(self.up)

        return score
