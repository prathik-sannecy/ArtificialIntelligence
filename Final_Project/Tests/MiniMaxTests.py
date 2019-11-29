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
    def test_MinValue(self):
        StateTree = BinaryTreeNode(2)
        StateTree.left = BinaryTreeNode(6)
        StateTree.right = BinaryTreeNode(2)
        StateTree.left.left = BinaryTreeNode(3)
        StateTree.left.right = BinaryTreeNode(4)
        StateTree.right.left = BinaryTreeNode(1)
        StateTree.right.right = BinaryTreeNode(7)

        testState = TestState(StateTree)
        assert(MinValue(testState) == 4)




if __name__ == '__main__':
    unittest.main()
