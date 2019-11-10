from  HW3.Learning import *

def ParseCSV(csvFileName):
    parsedCSV = []

    with open(csvFileName) as csvFile:
        for line in csvFile:
            parsedCSV.append(list(map(int, line.strip().split(','))))
    return parsedCSV



def main():

    trainingSet = ParseCSV('HW3_Files/spect-resplit-itg.train.csv')
    instanceCount, featureCount = Learn(trainingSet)
    print(instanceCount, featureCount)
    testingSet = ParseCSV('HW3_Files/spect-resplit-itg.test.csv')
    actual = [testingSet[x][0] for x in range(len(testingSet))]
    print(actual)

    calculated = []
    for testInstance in testingSet:

        testInstanceFeatures = testInstance[1:]
        classifyTestInstance = ClassifyInstance(testInstanceFeatures, featureCount, instanceCount)
        calculated.append(classifyTestInstance)
    print(calculated)

if __name__ == "__main__":
    main()