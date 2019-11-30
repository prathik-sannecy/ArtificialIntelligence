from copy import copy, deepcopy

class GameState:
    """Current State of the game"""
    def __init__(self):
        self.board = [5*[5*[None]]]  # 5x5 board
        self.numWhite = 0
        self.numBlack = 0
        self.passCount = 0
        self.stoneGroups = {}
        self.turn = 'B'

    def Utility(self):
        """Heuristic to keep track of who's ahead. Black stone = +1, white stone = -1

        inputs:
            None
        returns:
            (int)heuristic: number of black stones - number of white stones
        """
        return self.numBlack - self.numWhite

    def TerminalTest(self):
        """Returns whether the current state of the game indicates that it's terminated.
        Game is over if there are two consecutive passes, or if all the spots on the board are filled

        inputs:
            None
        returns:
            (bool)finished: whether the game is over or not
        """
        if self.passCount == 2 or self.numWhite + self.numBlack == 25:
            return True
        return False

    def GetActions(self):
        """Returns all valid moves (besides pass) for the current player

        inputs:
            None
        returns:
            (List[tuple((int), (int))])validActions: all valid locations to put a stone for the current player's move
        """
        actions = []
        # Check every empty spot on the board. If it is legal for the player to place their stone their, include it in the valid actions list
        for rowIndex, row in enumerate(self.board):
            for colIndex, dot in enumerate(row):
                if dot == None:
                    if self.IsLegal(self.stoneGroups, self.board, (rowIndex, colIndex)):
                        actions.append((rowIndex, colIndex))
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

        checkedOpposite = 5 * [5 * [0]]  # keeping track of whether piece is already checked
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
                        if self.IsGroupTrapped(localStoneGroup, localBoard, (x, y)):
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
        """Updates the count of black and white stones on the board

        inputs:
            None
        returns:
            None
        """
        self.numBlack = 0
        self.numWhite = 0
        for row in self.board:
            for stone in row:
                if stone == 'B':
                    self.numBlack += 1
                elif stone == 'W':
                    self.numWhite += 1

    def IsGroupTrapped(self, stoneGroup, board, exampleStoneInGroup):
        """Check's whether a stone's group is trapped or not. This means that there is not empty spaces around the group, and at least 1 outer edge

        inputs:
            (tuple((int), (int)))exampleStoneInGroup: stone within the group
            (Dict[(tuple((int), (int)))] : set{(tuple((int), (int)))})stoneGroup: current grouping of stones
            (List[(List[(int)])])board: current state of the board, with stone locations
        returns:
            (bool)trapped: true if the exampleStoneInGroup's group is trapped or not
        """
        edge = False
        # The only way the stone can flip color to the oppositions is if it's group is surrounded by the opposition's stone, and at least 1 edge
        for stone in stoneGroup[exampleStoneInGroup]:  # Check all stones in a group
            stoneX = stone[0]
            stoneY = stone[1]
            # See whether there are any empty spaces around the stone. If there are, then it is a legal move
            for x in range(stoneX - 1, stoneX + 2):
                for y in range(stoneY - 1, stoneY + 2):
                    # Ignore diagonals, and the the stone itself
                    if (abs(x - stoneX) + abs(y - stoneY)) is not 1:
                        continue
                    # Check whether the group has an edge surrounding it
                    if x < 0 or x > 4 or y < 0 or y > 4:
                        edge = True
                        continue
                    # At least one empty spot, so not trapped, which makes the move legal
                    if board[x][y] is None:
                        return False
        # If there aren't any empty spots surrounding the group, and there is an edge, then the group is trapped, which is not legal
        if edge:
            return True
        return False


    def IsLegal(self, stoneGroup, board, action):
        """Checks whether a player's move is legal or not

        inputs:
            (tuple((int), (int)))action: where to add the new stone
            (Dict[(tuple((int), (int)))] : set{(tuple((int), (int)))})stoneGroup: current grouping of stones
            (List[(List[(int)])])board: current state of the board, with stone locations
        returns:
            (bool)valid: whether the move is legal or not
        """
        # Approach is to assume that the move is legal, unless the board ends up in a state that indicates otherwise

        # Create copies to do calculations on
        localBoard = self.CopyBoard(board)
        localStoneGroup = self.CopyStoneGroups(stoneGroup)

        actionX = action[0]
        actionY = action[1]

        # Update the board and the stoneGroup with this new action
        localStoneGroup[action] = {action}
        localBoard[actionX][actionY] = self.turn
        self.MergeNeighboringStones(action, localStoneGroup, localBoard)

        # Now see whether this actions was actually valid or not
        # It is not legal if it causes the current player's stones to flip to the opposition's color because it is trapped
        return not self.IsGroupTrapped(localStoneGroup, localBoard, action)


    def MergeGroups(self, stoneGroup, val1, val2):
        """Merge two separate stone groups together

        inputs:
            (Dict[(tuple((int), (int)))] : set{(tuple((int), (int)))})stoneGroup: current grouping of stones
            (tuple((int), (int)))val1: stone within group1
            (tuple((int), (int)))val2: stone within group2
        """
        # Go through each stone in each group. Merge the groups that each stone points to
        for stone in stoneGroup[val1]:
            self.MergeSetsInDict(stoneGroup, stone, val2)
        for stone in stoneGroup[val2]:
            self.MergeSetsInDict(stoneGroup, stone, val1)

    def MergeSetsInDict(self, dictionary, val1, val2):
        """Given a dictionary where keys map to sets, merge the sets of two keys and have them both map to this new set

        inputs:
            (Dict[(obj)] : set{})dictionary: dictionary with keys mapping to set
            (obj)val1: first key to merge
            (obj)val2: second key to merge

        returns:
            None
        """
        dictionary[val1] = dictionary[val1] | dictionary[val2]
        dictionary[val2] = dictionary[val1] | dictionary[val2]

    def MergeNeighboringStones(self, action, stoneGroup, board):
        """When adding a new stone, add it to surrounding stone groups (that have stones of the same color)

        inputs:
            (tuple((int), (int)))action: where to add the new stone
            (Dict[(tuple((int), (int)))] : set{(tuple((int), (int)))})stoneGroup: current grouping of stones
            (List[(List[(int)])])board: current state of the board, with stone locations
        returns:
            None
        """
        actionX = action[0]
        actionY = action[1]
        for _ in range(2):  # Do it twice, to make sure all neighbors are updated since first pass
            # Check all direct neighbors of the new stone on the grid
            for x in range(actionX - 1, actionX + 2):
                for y in range(actionY - 1, actionY + 2):
                    # Ignore stone itself, and diagonals
                    if (abs(x - actionX) + abs(y - actionY)) is not 1:
                        continue
                    # Make sure neighbors are on the grid
                    if x < 0 or x > 4 or y < 0 or y > 4:
                        continue
                    # Ignore the case where the neighbor is None
                    if board[x][y] == None:
                        continue
                    # If the neighbor's color matches the new stone's color merge the neighbor's group with the new stone's group
                    if board[x][y] == board[actionX][actionY]:
                        self.MergeSetsInDict(stoneGroup, (x, y), (actionX, actionY))

    def CopyBoard(self, board):
        """Returns a copy of the input board

        inputs:
            (List[(List[(int)])])board
        returns:
            (List[(List[(int)])])boardCopy
        """
        return deepcopy(board)

    def CopyStoneGroups(self, stoneGroup):
        """Returns a copy of the stone Groups

        inputs:
            (Dict[(tuple((int), (int)))] : set{(tuple((int), (int)))})stoneGroup
        returns:
            (Dict[(tuple((int), (int)))] : set{(tuple((int), (int)))})stoneGroupCopy
        """
        return dict(stoneGroup)
