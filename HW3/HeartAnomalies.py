from  HW3.NaiveBayesianLearning import *

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

def main():
    """TODO
    """
    trainingSet = ParseCSV('HW3_Files/spect-itg.train.csv')
    instanceCount, featureCount = Learn(trainingSet)
    print(instanceCount, featureCount)
    testingSet = ParseCSV('HW3_Files/spect-itg.test.csv')
    actual = [testingSet[x][0] for x in range(len(testingSet))]
    print(actual)

    calculated = []
    for testInstance in testingSet:

        testInstanceFeatures = testInstance[1:]
        classifyTestInstance = ClassifyInstance(testInstanceFeatures, featureCount, instanceCount)
        calculated.append(classifyTestInstance)
    print(calculated)
    correct = 0
    for i in range(len(calculated)):
        if actual[i] == calculated[i]:
            correct += 1
    print(float(correct)/float(len(actual)))


if __name__ == "__main__":
    main()
