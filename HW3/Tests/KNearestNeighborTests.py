import unittest
from HW3.KNearestNeighbor import *


class NaiveBayesianLearningTests(unittest.TestCase):
    def test_ClassifyKNearestNeighbor(self):
        trainingSet = [
            [0, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1]
        ]
        instance = [1, 0, 1, 1, 0]

        classification = ClassifyKNearestNeighbor(trainingSet, instance, 3)
        print(classification)
        assert(classification == 0)


if __name__ == '__main__':
    unittest.main()
