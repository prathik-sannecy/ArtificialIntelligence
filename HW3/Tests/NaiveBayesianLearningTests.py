import unittest
from HW3.NaiveBayesianLearning import *


class NaiveBayesianLearningTests(unittest.TestCase):
    def test_Learn(self):
        trainingSet = []
        NUM_INSTANCE = 2**4
        for i in range(NUM_INSTANCE):
            instance = []
            classification = i % 2
            instance.append(classification)

            features = []

            while len(features) < math.log(NUM_INSTANCE):
                features.append(math.floor(i / (2**(len(features)+ 1))) % 2)

            instance += features
            trainingSet.append(instance)
        instanceCount, featureCount = Learn(trainingSet)
        assert(instanceCount == [8, 8])
        assert(featureCount[0] == [4, 4, 4])
        assert(featureCount[1] == [4, 4, 4])

    def test_ComputeLikelyhoodOfClassification(self):

        trainingSet = []
        trainingSet.append([0, 0, 1, 1])
        trainingSet.append([1, 1, 1, 1])
        instanceCount, featureCount = Learn(trainingSet)
        instanceFeatures = [1, 1, 1]
        likelyHood0 = ComputeLikelyhoodOfClassification(instanceFeatures, featureCount, instanceCount, 0)
        likelyHood1 = ComputeLikelyhoodOfClassification(instanceFeatures, featureCount, instanceCount, 1)
        assert (likelyHood1 > likelyHood0)

        trainingSet.append([0, 0, 0, 0])
        instanceCount, featureCount = Learn(trainingSet)
        instanceFeatures = [0, 0, 0]
        likelyHood0 = ComputeLikelyhoodOfClassification(instanceFeatures, featureCount, instanceCount, 0)
        likelyHood1 = ComputeLikelyhoodOfClassification(instanceFeatures, featureCount, instanceCount, 1)
        assert (likelyHood1 < likelyHood0)

    def test_ClassifyInstance(self):
        trainingSet = []
        trainingSet.append([0, 0, 1, 1])
        trainingSet.append([1, 1, 1, 1])
        instanceCount, featureCount = Learn(trainingSet)
        instanceFeatures = [1, 1, 1]
        classification = ClassifyInstance(instanceFeatures, featureCount, instanceCount)
        assert (classification == 1)

if __name__ == '__main__':
    unittest.main()
