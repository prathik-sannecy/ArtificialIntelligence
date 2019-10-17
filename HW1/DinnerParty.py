from Error import *

def Calc(persons):
    """Calculate the total score of the dinner table

    inputs:
        the people at the table
    returns:
        the total score of the table
    """
    score = 0
    for person in persons:
        score += person.GetScore()
    return score

