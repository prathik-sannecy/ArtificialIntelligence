import unittest
from Final_Project.MiniMax import *
import random


class BinaryTreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class TestState:
    def __init__(self, stateTree):
        self.stateTree = stateTree

    def Utility(self):
        return self.stateTree.val

    def TerminalTest(self):
        if self.stateTree.left is None and self.stateTree.right is None:
            return True
        return False

    def GetActions(self):
        return self.stateTree.left, self.stateTree.right

    def Result(self, action):
        self.stateTree = action
        return self


class TestMinMax(unittest.TestCase):
    # StatesTree looks like the following:
    #          2
    #        /   \
    #       6      2
    #      / \    / \
    #     3   7  1   4

    def InitializeTestState(self):
        StateTree = BinaryTreeNode(2)
        StateTree.left = BinaryTreeNode(6)
        StateTree.right = BinaryTreeNode(2)
        StateTree.left.left = BinaryTreeNode(3)
        StateTree.left.right = BinaryTreeNode(7)
        StateTree.right.left = BinaryTreeNode(1)
        StateTree.right.right = BinaryTreeNode(4)
        return TestState(StateTree)


    def test_MinValue(self):
        testState = self.InitializeTestState()
        assert(MinValue(testState) == 4)

    def test_MaxValue(self):
        testState = self.InitializeTestState()
        assert(MaxValue(testState) == 3)

    def test_MiniMaxDecision(self):
        testState = self.InitializeTestState()
        assert(MiniMaxDecision(testState).val == 6)

    def test_MinValueDepth(self):
        testState = self.InitializeTestState()
        assert(MinValue(testState, 2) == 2)

    def test_MaxValueDepth(self):
        testState = self.InitializeTestState()
        assert(MaxValue(testState, 2) == 6)

    def test_MiniMaxDecisionDepth(self):
        testState = self.InitializeTestState()
        assert(MiniMaxDecision(testState, 3).val == 6)




if __name__ == '__main__':
    unittest.main()
