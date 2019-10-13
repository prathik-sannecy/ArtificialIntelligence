from DinnerParty import *
from copy import deepcopy, copy

def Swap( person1, person2):
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


    tempPerson1AdjLeft = copy(person1.GetAdjLeft())
    tempPerson1AdjRight = copy(person1.GetAdjRight())
    tempPerson1Down = copy(person1.GetDown())
    tempPerson1Up = copy(person1.GetUp())

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









def Optomize(persons, lowest, next_lowest):
    pass