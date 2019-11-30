from copy import copy, deepcopy

class GameState:
    def __init__(self):
        self.board = [5*[5*[None]]]  # 5x5 board
        self.numWhite = 0
        self.numBlack = 0
        self.passCount = 0
        self.stoneGroups = {}
        self.turn = 'B'

    def Utility(self):
        return self.numBlack - self.numWhite

    def TerminalTest(self):
        if self.passCount == 2 or self.numWhite + self.numBlack == 25:
            return True
        return False

    def GetActions(self):
        actions = []
        localBoard = self.CopyBoard(self.board)
        for rowIndex, row in enumerate(localBoard):
            for colIndex, dot in enumerate(row):
                if dot == None:
                    if self.IsLegal(self.stoneGroups, self.board, self.turn, (rowIndex, colIndex)):
                        localBoard[rowIndex][colIndex] = self.turn
                        actions.append((rowIndex, colIndex))
                        localBoard = self.board
        return actions

    def Result(self, action):
        localBoard = self.CopyBoard(self.board)
        actionX = action[0]
        actionY = action[1]

        localStoneGroup = self.CopyStoneGroups(self.stoneGroups)
        localStoneGroup[action] = set()
        localStoneGroup[action].add(action)

        self.MergeNeighborHashes(action, localStoneGroup, localBoard)
        # Do it twice, to make sure all neighbors are updated
        self.MergeNeighborHashes(action, localStoneGroup, localBoard)


        # Check to see if surrounding any white groups

        # Update the group and add to current if it is surrounded. Also, update the count of pieces
        checkedOpposite = [5 * [5 * [0]]]  # keeping track of whether peice is already checked
        for piece in localStoneGroup[(actionX, actionY)]: # Check all pieces in a group
            if localBoard[piece[0]+1][piece[1]] is not localBoard[piece[0]][piece[1]] and checkedOpposite[piece[0]+1][piece[1]] == 0:  # If opponents piece is a neighbor
                for groupMate in localStoneGroup[piece[0]][piece[1]]:  # Make sure that the opponent's piece's group is not trapped
                    if localBoard[groupMate[0]+1][groupMate[1]] == None:
                        break

        checkedOpposite = [5 * [5 * [0]]]  # keeping track of whether peice is already checked
        for stone in localStoneGroup[action]: # Check all pieces in a group
            stoneX = stone[0]
            stoneY = stone[1]
            for x in range(stoneX - 1, stoneX + 2):
                for y in range(stoneY - 1, stoneY + 2):
                    if x == stoneX and y == stoneY:
                        continue
                    elif x < 0 or x > 4 or y < 0 or y > 4:
                        continue
                    elif localBoard[x][y] is None:
                        continue
                    elif checkedOpposite[x][y] == 1:
                        continue
                    elif localBoard[x][y] is not self.turn:
                        for oppStone in localStoneGroup[(x, y)]:
                            oppStoneX = oppStone[0]
                            oppStoneY = oppStone[1]
                            checkedOpposite[oppStoneX][oppStoneY] = 1






        return self

    def IsLegal(self, stoneGroup, board, turn, action):
        localBoard = self.CopyBoard(self.board)
        localStoneGroup = self.CopyStoneGroups(self.stoneGroups)

        self.MergeNeighborHashes(action, localStoneGroup, localBoard)
        # Do it twice, to make sure all neighbors are updated
        self.MergeNeighborHashes(action, localStoneGroup, localBoard)


        for stone in stoneGroup[action]:  # Check all pieces in a group
            stoneX = stone[0]
            stoneY = stone[1]

            edge = False
            for x in range(stoneX - 1, stoneX + 2):
                for y in range(stoneY - 1, stoneY + 2):
                    if x == stoneX and y == stoneY:
                        continue
                    if x < 0 or x > 4 or y < 0 or y > 4:
                        edge = True
                        continue
                    if board[x][y] is None:
                        return True
            if edge:
                return False
            return True


    def MergeGroups(self, stoneGroup, val1, val2):
        for stone in stoneGroup[val1]:
            self.MergeSetsInDict(stoneGroup, stone, val2)
        for stone in stoneGroup[val2]:
            self.MergeSetsInDict(stoneGroup, stone, val1)

    def MergeSetsInDict(self, dictionary, val1, val2):
        dictionary[val1] = dictionary[val1] | dictionary[val2]
        dictionary[val2] = dictionary[val1] | dictionary[val2]

    def MergeNeighborHashes(self, action, stoneGroup, board):
        actionX = action[0]
        actionY = action[1]
        for x in range(actionX - 1, actionX + 2):
            for y in range(actionY - 1, actionY + 2):
                if x == actionX and y == actionY:
                    continue
                if x < 0 or x > 4 or y < 0 or y > 4:
                    continue
                if board[x][y] == self.turn:
                    self.MergeSetsInDict(stoneGroup, (x, y), (actionX, actionY))

    def CopyBoard(self, board):
        return deepcopy(board)

    def CopyStoneGroups(self, stoneGroups):
        return dict(stoneGroups)