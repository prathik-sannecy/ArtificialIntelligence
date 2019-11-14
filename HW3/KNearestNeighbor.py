def ClassifyKNearestNeighbor(trainingSet, newInstanceFeatures, k):
    difference = []
    classificationIndex = 0
    featureStartIndex = 1  # Feature offset in an instance
    for instance in trainingSet:
        classification = instance[classificationIndex]
        instanceFeatures = instance[featureStartIndex:]  # Filter out classification
        difference.append((sum([abs(instanceFeatures[k] - newInstanceFeatures[k]) for k in range(len(newInstanceFeatures))]), classification))
    kdifference = sorted(difference)[:k]
    zeroCount = 0
    for diff in kdifference:
        if diff[1] == 0:
            zeroCount += 1
    if zeroCount > k/2:
        return 0
    return 1
