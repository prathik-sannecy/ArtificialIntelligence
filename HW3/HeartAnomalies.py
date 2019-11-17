from  NaiveBayesianLearning import *
from  KNearestNeighbor import *
from random import shuffle

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
    """Runs the Naive Bayesian Learning/classification on the training set, and tests it with the testing set

    inputs:
        (List[(int)])trainingSet: the Naive Bayesian Learning training set
        (List[(int)])testingSet: set to test the trained Naive Bayesian data structure

    returns:
        (List[(int)])calculated: the calculated classification of each testing instance in the testing set
    """
    instanceCount, featureCount = Learn(trainingSet)

    calculated = []
    for testInstance in testingSet:
        testInstanceFeatures = testInstance[1:]
        classifyTestInstance = ClassifyInstance(testInstanceFeatures, featureCount, instanceCount)
        calculated.append(classifyTestInstance)
    return  calculated

def RunKNearestNeighbor(trainingSet, testingSet):
    """Runs the KNN Learning/classification on the training set, and tests it with the testing set

    inputs:
        (List[(int)])trainingSet: the KNN training set
        (List[(int)])testingSet: set to test the trained Naive Bayesian data structure

    returns:
        (List[(int)])calculated: the calculated classification of each testing instance in the testing set
    """
    calculated = []
    for testInstance in testingSet:
        testInstanceFeatures = testInstance[1:]
        classifyTestInstance = ClassifyKNearestNeighbor(trainingSet,testInstanceFeatures, 5)
        calculated.append(classifyTestInstance)
    return calculated

def GetLearningFunctionAccuracy(trainingSetName, testingSetName, learningFunction):
    trainingSet = ParseCSV(trainingSetName)
    testingSet = ParseCSV(testingSetName)
    shuffle(trainingSet)

    actual = [testingSet[x][0] for x in range(len(testingSet))]
    lenActual = len(actual)

    calculated = learningFunction(trainingSet, testingSet)
    correctZeroCount = 0
    correctOneCount = 0
    actualZeroCount = 0
    actualOneCount = 0
    for i in range(len(actual)):
        if actual[i] == 1:
            actualOneCount += 1
            if actual[i] == calculated[i]:
                correctOneCount += 1
        else:
            actualZeroCount += 1
            if actual[i] == calculated[i]:
                correctZeroCount += 1

    totalCorrect = correctZeroCount + correctOneCount
    accuracy = float(totalCorrect) / float(lenActual)
    abnormalCorrect = float(correctZeroCount) / float(actualZeroCount)
    normalCorrect = float(correctOneCount) / float(actualOneCount)

    print(str(totalCorrect) + "/" + str(lenActual) + "(" + str(accuracy) + ") " + str(correctZeroCount) + "/" + str(actualZeroCount) + "(" + str(abnormalCorrect) + ") " + str(correctOneCount) + "/" + str(actualOneCount) + "(" + str(normalCorrect) + ") ")



def main():

    datasets = (('HW3_Files/spect-itg.train.csv', 'HW3_Files/spect-itg.test.csv'),('HW3_Files/spect-orig.train.csv', 'HW3_Files/spect-orig.test.csv'), ('HW3_Files/spect-resplit.train.csv', 'HW3_Files/spect-resplit.test.csv'), ('HW3_Files/spect-resplit-itg.train.csv', 'HW3_Files/spect-resplit-itg.test.csv'))

    print("Naive Bayesian Algorithm")
    for set in datasets:
        trainingSetName = set[0]
        testingSetName = set[1]
        print(trainingSetName.split("/")[1].split(".")[0], end=" ")
        GetLearningFunctionAccuracy(trainingSetName, testingSetName, RunNaiveBayesianLearning)

    print("\n")

    print("K-Nearest-Neighbor Algorithm")
    for set in datasets:
        trainingSetName = set[0]
        testingSetName = set[1]
        print(trainingSetName.split("/")[1].split(".")[0], end=" ")
        GetLearningFunctionAccuracy(trainingSetName, testingSetName, RunKNearestNeighbor)

if __name__ == "__main__":
    main()
