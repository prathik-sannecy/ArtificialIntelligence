import unittest
from Final_Project.GameState import *
import random



class TestGameState(unittest.TestCase):
    # GameState looks like this:
    # B-WBW
    # WWB--
    # -----
    # WWWWB
    # BWBBB

    def test_GameStateCopyBoard(self):
        gameState = GameState()
        board = self.InitilizeGameStateBoard()
        boardCopy = gameState.CopyBoard(board)
        for rowIndex, row in enumerate(board):
            for colIndex, stone in enumerate(row):
                assert(stone == boardCopy[rowIndex][colIndex])

    def test_GameStateCopyStoneGroups(self):
        gameState = GameState()
        stoneGroups = self.InitializeGameStateStoneGroups()
        stoneGroupsCopy = gameState.CopyStoneGroups(stoneGroups)
        for stone in stoneGroups:
            assert(stoneGroups[stone] == stoneGroupsCopy[stone])

    def test_GameStateIsLegal(self):
        gameState = GameState()
        stoneGroups = self.InitializeGameStateStoneGroups()
        board = self.InitilizeGameStateBoard()

        assert(gameState.IsLegal(stoneGroups, board, (0, 1)) == False)
        assert(gameState.IsLegal(stoneGroups, board, (1, 3)) == True)

    def test_MergeSetsInDict(self):
        gameState = GameState()
        stoneGroups = self.InitializeGameStateStoneGroups()
        testDict = {}
        testDict[(0, 0)] = {(0, 0)}
        testDict[(1, 1)] = {(1, 1)}

        gameState.MergeSetsInDict(testDict, (0, 0), (1, 1))

        assert(((0, 0) in testDict[(0, 0)]) == True)
        assert(((1, 1) in testDict[(0, 0)]) == True)
        assert(((0, 0) in testDict[(1, 1)]) == True)
        assert(((1, 1) in testDict[(1, 1)]) == True)

    def test_MergeGroups(self):
        gameState = GameState()
        stoneGroups = self.InitializeGameStateStoneGroups()

        gameState.MergeGroups(stoneGroups, (3, 0), (3, 4))

        assert(((3, 1) in stoneGroups[(4, 2)]) == True)
        for stone in stoneGroups[(3, 0)]:
            assert((stone in stoneGroups[3, 4]) == True)
        for stone in stoneGroups[(3, 4)]:
            assert((stone in stoneGroups[3, 0]) == True)

    def test_MergeNeighboringStones(self):
        gameState = GameState()
        stoneGroups = self.InitializeGameStateStoneGroups()
        board = self.InitilizeGameStateBoard()
        board[2][0] = 'W'
        stoneGroups[(2, 0)] = {(2, 0)}

        gameState.MergeNeighboringStones((2, 0), stoneGroups, board)
        gameState.MergeNeighboringStones((2, 0), stoneGroups, board)

        assert(((2, 0) in stoneGroups[(3, 0)]) == True)
        for stone in stoneGroups[(3, 0)]:
            assert((stone in stoneGroups[2, 0]) == True)
        for stone in stoneGroups[(2, 0)]:
            assert((stone in stoneGroups[3, 0]) == True)


    def InitilizeGameStateBoard(self):
        return [
            ['B', None, 'W', 'B', 'W'],
            ['W', 'W', 'B', None, None],
            [None, None, None, None, None],
            ['W', 'W', 'W', 'W', 'B'],
            ['B', 'W', 'B', 'B', 'B']
        ]

    def InitializeGameStateStoneGroups(self):
        stoneGroups = {}
        stoneGroups[(0, 0)] = {(0, 0)}
        stoneGroups[(0, 2)] = {(0, 2)}
        stoneGroups[(0, 3)] = {(0, 3)}
        stoneGroups[(0, 4)] = {(0, 4)}
        stoneGroups[(1, 0)] = {(1, 0), (1, 1)}
        stoneGroups[(1, 1)] = {(1, 0), (1, 1)}
        stoneGroups[(1, 2)] = {(1, 2)}
        stoneGroups[(3, 0)] = {(3, 0), (3, 1), (3, 2), (3, 3), (4, 1)}
        stoneGroups[(3, 1)] = {(3, 0), (3, 1), (3, 2), (3, 3), (4, 1)}
        stoneGroups[(3, 2)] = {(3, 0), (3, 1), (3, 2), (3, 3), (4, 1)}
        stoneGroups[(3, 3)] = {(3, 0), (3, 1), (3, 2), (3, 3), (4, 1)}
        stoneGroups[(3, 4)] = {(4, 2), (4, 3), (4, 4), (3, 4)}
        stoneGroups[(4, 0)] = {(4, 0)}
        stoneGroups[(4, 1)] = {(3, 0), (3, 1), (3, 2), (3, 3), (4, 1)}
        stoneGroups[(4, 2)] = {(4, 2), (4, 3), (4, 4), (3, 4)}
        stoneGroups[(4, 3)] = {(4, 2), (4, 3), (4, 4), (3, 4)}
        stoneGroups[(4, 4)] = {(4, 2), (4, 3), (4, 4), (3, 4)}

        return stoneGroups

if __name__ == '__main__':
    unittest.main()
