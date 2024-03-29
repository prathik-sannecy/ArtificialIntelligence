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

    def HammingDistance(arr1, arr2):
        """Returns the Hamming distance between two arrays (that hold only '0' or '1')

        inputs:
            (List[(int)])arr1
            (List[(int)])arr2

        returns:
            (int)hammingDistance: the Hamming distance between arr1 and arr2
        """
        hammingDistance = 0
        assert(len(arr1) == len(arr2))
        for k in range(len(arr1)):
            if arr1[k] is not arr2[k]:
                hammingDistance += 1
        return hammingDistance


    difference = []
    classificationIndex = 0
    featureStartIndex = 1  # Feature offset in an instance
    for instance in trainingSet:
        classification = instance[classificationIndex]
        instanceFeatures = instance[featureStartIndex:]  # Filter out classification
        # the Hamming distance between a feature set and its neighbors
        difference.append((HammingDistance(instanceFeatures, newInstanceFeatures), classification))
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
