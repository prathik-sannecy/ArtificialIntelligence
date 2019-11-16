def ClassifyKNearestNeighbor(trainingSet, newInstanceFeatures, k):
    """Returns how a feature list should be classified based on how well it matches to its nearest neighbors (k
    nearest neighbors algorithm)

    inputs:
        (List[(int)])trainingSet: Training set in the following format:
            Instance0 classification, Instance0 feature0, Instance0 feature1...Instance0 featureN
            Instance1 classification, Instance0 feature1, Instance1 feature1...Instance1 featureN
        (list[(int)])newInstanceFeatures: a feature list to be classified
        (int)k: how many nearest neighbors to compare to

    returns:
        (int)classification: whether the feature list should be classified as '0' or '1'
    """

    difference = []
    classificationIndex = 0
    featureStartIndex = 1  # Feature offset in an instance
    for instance in trainingSet:
        classification = instance[classificationIndex]
        instanceFeatures = instance[featureStartIndex:]  # Filter out classification
        # the total difference between a neighbor and the feature set is the sum of all the differences per feature
        difference.append((sum([abs(instanceFeatures[k] - newInstanceFeatures[k]) for k in range(len(newInstanceFeatures))]), classification))
    # Pick the k nearest neighbors with the most matching features
    kdifference = sorted(difference)[:k]
    # Return the classification that the majority of features have
    zeroCount = 0
    for diff in kdifference:
        if diff[1] == 0:
            zeroCount += 1
    if zeroCount > float(k)/2:
        return 0
    return 1
