import math

def Learn(trainingSet):
    """Naive Bayesian learning algorithm

    inputs:
        (List) Training set in the following format:
        Instance0 classification, Instance0 feature0, Instance0 feature1...Instance0 featureN
        Instance1 classification, Instance0 feature1, Instance1 feature1...Instance1 featureN
        ...

    returns:
        (tuple) (count of instances with a classification,
        count of instances with a particular feature within a classification)
    """
    classificationIndex = 0
    featureStartIndex = 1  # Feature offset in an instance
    numInstances = len(trainingSet)
    numFeatures = len(trainingSet[0]) - 1  # each instance has 1 classification item, the rest are features
    # Initialize featureCount (counts of features for a particular classification)
    featureCount = []
    featureCount.append(numFeatures * [0])
    featureCount.append(numFeatures * [0])
    # Initialize instanceCount (counts of instances for a particular classification)
    instanceCount = [0, 0]
    for instance in trainingSet:
        classification = instance[classificationIndex]
        instanceCount[classification] += 1  # Keep running count of number of instances with of a classification
        instanceFeatures = instance[featureStartIndex:]  # Filter out classification
        # Keep a running count of number of instances with a particular feature (per classification)
        for featureIndex in range(numFeatures):
            if instanceFeatures[featureIndex] == 1:
                featureCount[classificationIndex][featureIndex] += 1
    return instanceCount, featureCount

def ComputeLikelyhoodOfClassification(instanceFeatures, featureCount, instanceCount, classification):
    likelyHood = math.log(instanceCount[classification] + .5) - math.log(instanceCount[0] + instanceCount[1] + .5)
    numFeatures = len(instanceFeatures)
    for featureIndex in range(numFeatures):
        countOfFeature = featureCount[classification][featureIndex]
        if instanceFeatures[featureIndex] == 0:
            countOfFeature = instanceCount[classification]
        likelyHood += math.log(countOfFeature + .5) - math.log(instanceCount[classification] + .5)
    return likelyHood

def classifyInstance(instanceFeatures, featureCount, instanceCount):
    if ComputeLikelyhoodOfClassification(instanceFeatures, featureCount, instanceCount, 1) > ComputeLikelyhoodOfClassification(instanceFeatures, featureCount, instanceCount, 0):
        return 1
    return 0
