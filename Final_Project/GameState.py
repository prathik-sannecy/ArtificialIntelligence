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
                    if self.IsLegal(self.stoneGroups, self.board, (rowIndex, colIndex)):
                        localBoard[rowIndex][colIndex] = self.turn
                        actions.append((rowIndex, colIndex))
                        localBoard = self.CopyBoard(self.board)
        return actions

    def Result(self, action):
        localBoard = self.CopyBoard(self.board)
        actionX = action[0]
        actionY = action[1]

        localStoneGroup = self.CopyStoneGroups(self.stoneGroups)
        localStoneGroup[action] = set()
        localStoneGroup[action].add(action)
        localBoard[actionX][actionY] = self.turn

        self.MergeNeighboringStones(action, localStoneGroup, localBoard)

        checkedOpposite = 5 * [5 * [0]]  # keeping track of whether peice is already checked
        for stone in localStoneGroup[action]: # Check all pieces in a group
            stoneX = stone[0]
            stoneY = stone[1]
            for x in range(stoneX - 1, stoneX + 2):
                for y in range(stoneY - 1, stoneY + 2):
                    if (abs(x - stoneX) + abs(y - stoneY)) is not 1:
                        continue
                    elif x < 0 or x > 4 or y < 0 or y > 4:
                        continue
                    elif localBoard[x][y] is None:
                        continue
                    elif checkedOpposite[x][y] == 1:
                        continue
                    elif localBoard[x][y] is not self.turn:
                        if self.IsGroupSurrounded(localStoneGroup, localBoard, (x, y)):
                            self.MergeGroups(localStoneGroup, (x, y), stone)
                            for oppStone in localStoneGroup[(x, y)]:
                                oppStoneX = oppStone[0]
                                oppStoneY = oppStone[1]
                                localBoard[oppStoneX][oppStoneY] = self.turn

                                for oppX in range(oppStoneX - 1, oppStoneX + 2):
                                    for oppY in range(oppStoneY - 1, oppStoneY + 2):
                                        if (abs(oppX - oppStoneX) + abs(oppY - oppStoneY)) is not 1:
                                            continue
                                        if oppX < 0 or oppX > 4 or oppY < 0 or oppY > 4:
                                            continue
                                        if localBoard[oppX][oppY] is self.turn:
                                            self.MergeGroups(localStoneGroup, (oppX, oppY), stone)

                        for oppStone in localStoneGroup[(x, y)]:
                            oppStoneX = oppStone[0]
                            oppStoneY = oppStone[1]
                            checkedOpposite[oppStoneX][oppStoneY] = 1

        self.board = self.CopyBoard(localBoard)
        self.stoneGroups = self.CopyStoneGroups(localStoneGroup)

        self.UpdateStoneCount()

        return self

    def UpdateStoneCount(self):
        self.numBlack = 0
        self.numWhite = 0
        for row in self.board:
            for stone in row:
                if stone == 'B':
                    self.numBlack += 1
                elif stone == 'W':
                    self.numWhite += 1

    def IsGroupSurrounded(self, stoneGroup, board, exampleStoneInGroup):
        for stone in stoneGroup[exampleStoneInGroup]:
            stoneX = stone[0]
            stoneY = stone[1]

            for x in range(stoneX - 1, stoneX + 2):
                for y in range(stoneY - 1, stoneY + 2):
                    if (abs(x - stoneX) + abs(y - stoneY)) is not 1:
                        continue
                    if x < 0 or x > 4 or y < 0 or y > 4:
                        continue
                    if board[x][y] is None:
                        return False
        return True

    def IsLegal(self, stoneGroup, board, action):
        localBoard = self.CopyBoard(board)
        localStoneGroup = self.CopyStoneGroups(stoneGroup)

        actionX = action[0]
        actionY = action[1]

        localStoneGroup[action] = {action}
        localBoard[actionX][actionY] = self.turn

        self.MergeNeighboringStones(action, localStoneGroup, localBoard)



        edge = False
        for stone in localStoneGroup[action]:  # Check all pieces in a group
            stoneX = stone[0]
            stoneY = stone[1]

            for x in range(stoneX - 1, stoneX + 2):
                for y in range(stoneY - 1, stoneY + 2):
                    if (abs(x - stoneX) + abs(y - stoneY)) is not 1:
                        continue
                    if x < 0 or x > 4 or y < 0 or y > 4:
                        edge = True
                        continue
                    if localBoard[x][y] is None:
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

    def MergeNeighboringStones(self, action, stoneGroup, board):
        actionX = action[0]
        actionY = action[1]
        for _ in range (2):  # Do it twice, to make sure all neighbors are updated since first pass
            for x in range(actionX - 1, actionX + 2):
                for y in range(actionY - 1, actionY + 2):
                    if (abs(x - actionX) + abs(y - actionY)) is not 1:
                        continue
                    if x < 0 or x > 4 or y < 0 or y > 4:
                        continue
                    if board[x][y] == None:
                        continue
                    if board[x][y] == board[actionX][actionY]:
                        self.MergeSetsInDict(stoneGroup, (x, y), (actionX, actionY))

    def CopyBoard(self, board):
        return deepcopy(board)

    def CopyStoneGroups(self, stoneGroups):
        return dict(stoneGroups)