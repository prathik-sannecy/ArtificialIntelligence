import math

def Learn(trainingSet):
    """Naive Bayesian learning algorithm

    inputs:
        (List)trainingSet: Training set in the following format:
        Instance0 classification, Instance0 feature0, Instance0 feature1...Instance0 featureN
        Instance1 classification, Instance0 feature1, Instance1 feature1...Instance1 featureN
        ...

    returns:
        (tuple)(instanceCount, featureCount): (count of instances with a classification,
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
    """Returns the likelyhood that a particular feature list is of a certain classification based on Naive Bayesian learning algorithm

    inputs:
        (list)instanceFeatures: a feature list to be classified
        (list)featureCount: how many total(all instances) features are in each classification are in the training set
        (list)instanceCount: how many instances are in each classification are in the training set
        (int)classification: whether the feature list should be classified as '0' or '1'

    returns:
        (float)likelyHood: how likely the feature list fits the classification, based on the training set
    """
    # default is that likelyhood is dependant on how many instances we've already seen
    likelyHood = math.log(instanceCount[classification] + .5) - math.log(instanceCount[0] + instanceCount[1] + .5)
    numFeatures = len(instanceFeatures)
    # Adjust the likelyhood based on how many features of the classification it matches
    for featureIndex in range(numFeatures):
        countOfFeature = featureCount[classification][featureIndex]
        if instanceFeatures[featureIndex] == 0:
            countOfFeature = instanceCount[classification]
        likelyHood += math.log(countOfFeature + .5) - math.log(instanceCount[classification] + .5)
    return likelyHood

def classifyInstance(instanceFeatures, featureCount, instanceCount):
    """Returns how a feature list should be classified based on likelyhood

    inputs:
        (list)instanceFeatures: a feature list to be classified
        (list)featureCount: how many total(all instances) features are in each classification are in the training set
        (list)instanceCount: how many instances are in each classification are in the training set

    returns:
        (int)classification: whether the feature list should be classified as '0' or '1'
    """
    if ComputeLikelyhoodOfClassification(instanceFeatures, featureCount, instanceCount, 1) > ComputeLikelyhoodOfClassification(instanceFeatures, featureCount, instanceCount, 0):
        return 1
    return 0
