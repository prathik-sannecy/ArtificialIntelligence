import DinnerParty
import Person

def Swap(dinnerTable, element1Row, element1Col, element2Row, element2Col):
    temp = dinnerTable[element1Row][element1Col]
    dinnerTable[element1Row][element1Col] = dinnerTable[element2Row][element2Col]
    dinnerTable[element2Row][element2Col] = temp
    return dinnerTable

