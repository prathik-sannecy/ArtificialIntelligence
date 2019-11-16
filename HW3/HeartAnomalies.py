from  HW3.NaiveBayesianLearning import *
from  HW3.KNearestNeighbor import *

def ParseCSV(csvFileName):
    """Parse a CSV file of integers

    Inputs:
        (String)csvFileName: Name of CSV file to parse

    return:
        (list[list(int)]] parsedCSV: the CSV file parsed, containing only ints
    """
    parsedCSV = []

    with open(csvFileName) as csvFile:
        for line in csvFile:
            parsedCSV.append(list(map(int, line.strip().split(','))))
    return parsedCSV

def RunNaiveBayesianLearning(trainingSet, testingSet):
    """TODO
        """
    instanceCount, featureCount = Learn(trainingSet)

    calculated = []
    for testInstance in testingSet:
        testInstanceFeatures = testInstance[1:]
        classifyTestInstance = ClassifyInstance(testInstanceFeatures, featureCount, instanceCount)
        calculated.append(classifyTestInstance)
    return  calculated

def RunKNearestNeighbor(trainingSet, testingSet):
    """TODO
        """
    calculated = []
    for testInstance in testingSet:
        testInstanceFeatures = testInstance[1:]
        classifyTestInstance = ClassifyKNearestNeighbor(trainingSet,testInstanceFeatures, 7)
        calculated.append(classifyTestInstance)
    return calculated



def main():
    trainingSet = ParseCSV('HW3_Files/spect-itg.train.csv')

    testingSet = ParseCSV('HW3_Files/spect-itg.test.csv')
    actual = [testingSet[x][0] for x in range(len(testingSet))]

    calculated = RunKNearestNeighbor(trainingSet, testingSet)
    correct = 0
    for i in range(len(calculated)):
        if actual[i] == calculated[i]:
            correct += 1
    print(float(correct) / float(len(actual)))


if __name__ == "__main__":
    main()
