from CalculateScore import *
from Error import *
import random

def Swap(person1, person2):
    """Swaps 2 people's positions at the dinner table

    inputs:
        (People) person1
        (People) person2
    returns:
        None
    """
    # Get person1's neighbors to point at person2
    try:
        if person1.GetAdjLeft(): person1.GetAdjLeft().SetAdjRight(person2)
    except InvalidPersonOperation:
        pass
    try:
        if person1.GetAdjRight(): person1.GetAdjRight().SetAdjLeft(person2)
    except InvalidPersonOperation:
        pass
    try:
        if person1.GetDown(): person1.GetDown().SetUp(person2)
    except InvalidPersonOperation:
        pass
    try:
        if person1.GetUp(): person1.GetUp().SetDown(person2)
    except InvalidPersonOperation:
        pass

    # Get person2's neighbors to point at person1
    try:
        if person2.GetAdjLeft(): person2.GetAdjLeft().SetAdjRight(person1)
    except InvalidPersonOperation:
        pass
    try:
        if person2.GetAdjRight(): person2.GetAdjRight().SetAdjLeft(person1)
    except InvalidPersonOperation:
        pass
    try:
        if person2.GetDown(): person2.GetDown().SetUp(person1)
    except InvalidPersonOperation:
        pass
    try:
        if person2.GetUp(): person2.GetUp().SetDown(person1)
    except InvalidPersonOperation:
        pass

    # Temporarily store person1's neighbors (for swapping)
    tempPerson1AdjLeft = (person1.GetAdjLeft())
    tempPerson1AdjRight = (person1.GetAdjRight())
    tempPerson1Down = (person1.GetDown())
    tempPerson1Up = (person1.GetUp())

    # Get person1 to point at person2's neighbors
    try:
        person1.SetAdjLeft(person2.GetAdjLeft())
    except InvalidPersonOperation:
        person1.SetAdjLeft(person2)
    try:
        person1.SetAdjRight(person2.GetAdjRight())
    except InvalidPersonOperation:
        person1.SetAdjRight(person2)
    try:
        person1.SetDown(person2.GetDown())
    except InvalidPersonOperation:
        person1.SetDown(person2)
    try:
        person1.SetUp(person2.GetUp())
    except InvalidPersonOperation:
        person1.SetUp(person2)

    # Get person2 to point at person1's neighbors
    try:
        person2.SetAdjLeft(tempPerson1AdjLeft)
    except InvalidPersonOperation:
        person2.SetAdjLeft(person1)
    try:
        person2.SetAdjRight(tempPerson1AdjRight)
    except InvalidPersonOperation:
        person2.SetAdjRight(person1)
    try:
        person2.SetDown(tempPerson1Down)
    except InvalidPersonOperation:
        person2.SetDown(person1)
    try:
        person2.SetUp(tempPerson1Up)
    except InvalidPersonOperation:
        person2.SetUp(person1)

    # Swap person1/person2's corresponding 'position' at the table
    tempPerson1Position = person1.GetPosition()
    person1.SetPosition(person2.GetPosition())
    person2.SetPosition(tempPerson1Position)


def Optimize(persons, lowest, nextLowest, currentScore, randCounter = 0):
    """Algorithm to optomize the dinner table's seating arrangement score

    inputs:
        (list people) the people at the dinner table
        (int) the lowest score to swap (ie 0=person with lowest score, 1=person with second lowest score, etc)
        (int) the next lowest score to swap (ie 0=person with lowest score, 1=person with second lowest score, etc)
    returns:
        tuple(int score, list arrangement)
            score is the maximum table score
            arrangement is the seating arrangement that provides the score (index=person, value=position)
    """
    print(currentScore)
    personsLen = len(persons)
    # Sort the people from lowest to highest score
    persons.sort(key=lambda x: x.GetScore(), reverse=True)
    randCounter += 1
    if randCounter % int(personsLen ** 2) == 0:
        print("here")
        personASwap = random.randint(0, personsLen - 1)
        personBSwap = personASwap
        while personBSwap == personASwap:
            personBSwap = random.randint(0, personsLen - 1)
        Swap(persons[personASwap], persons[personBSwap])
        newScore = Calc(persons)
        return Optimize(persons, 0, 1, newScore, randCounter)

    # Swap the two people with the nth, mth lowest score
    Swap(persons[lowest], persons[nextLowest])
    newScore = Calc(persons)
    # if the new score after swap is better, restart the algorithm am the base addresses
    if newScore > currentScore:
        return Optimize(persons, 0, 1, newScore, randCounter)
    # If the score after the swap is not better...
    else:
        # Unswap
        Swap(persons[lowest], persons[nextLowest])
        # Figure out which next two people's position to swap
        # Strategy is to try to improve the lowest person's score
        # first by swapping with all other people, then the next
        # lowest person's score, and so on so forth
        if nextLowest == (len(persons) - 1):
            if lowest == nextLowest - 1:
                return currentScore, persons
            else:
                lowest += 1
                nextLowest = lowest + 1
                return Optimize(persons, lowest, nextLowest, currentScore, randCounter)
        else:
            return Optimize(persons, lowest, nextLowest + 1, currentScore, randCounter)
