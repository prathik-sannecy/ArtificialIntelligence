from Error import *

def Calc(persons):
    score = 0
    for person in persons:
        score += person.GetScore()
    return score


def DinnerParty():
    pass


if __name__ == "main":
    DinnerParty()

