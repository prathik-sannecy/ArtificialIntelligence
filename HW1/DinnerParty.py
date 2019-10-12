from Error import *

def Calc(dinnerTable):
    if not dinnerTable:
        raise BadPartyTableMatrix('Incorrect format of Dinner Party Table')


    topRow = dinnerTable[0]
    bottomRow = dinnerTable[1]

    return CalcAdjHostGuest(topRow) + CalcAdjHostGuest(bottomRow) + CalcOppHostGuest(dinnerTable)

def CalcAdjHostGuest(tableRow):
    sum = 0
    for column in range(0, len(tableRow) - 1):
        # +1 point if Host and Guest seated adjacent
        if tableRow[column].GetType() != tableRow[column + 1].GetType():
            sum += 1
        sum += tableRow[column].GetRelationTo(tableRow[column + 1].GetNumber())
        sum += tableRow[column + 1].GetRelationTo(tableRow[column].GetNumber())
    return sum

def CalcOppHostGuest(dinnerTable):
    sum = 0
    tableRowTop = dinnerTable[0]
    tableRowBottom = dinnerTable[1]
    for column in range(0, len(tableRowTop)):
        # +2 points if Host and Guest seated opposite
        if tableRowTop[column].GetType() != tableRowBottom[column].GetType():
            sum += 2
        sum += int(tableRowTop[column].GetRelationTo(tableRowBottom[column].GetNumber()))
        sum += int(tableRowBottom[column].GetRelationTo(tableRowTop[column].GetNumber()))
    return sum

def DinnerParty():
    pass


if __name__ == "main":
    DinnerParty()

