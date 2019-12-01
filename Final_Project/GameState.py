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
        actions.append("Pass")  # Player always has the option to pass
        return actions

    def Result(self, action):
        """Updates the game state after a player makes a move

        inputs:
            (tuple((int), (int)))action: where to add the new stone
        returns:
            (GameState)gameState: new state of the game after current move
        """
        # If the player decides to pass, then increment the passCount and let it be the other player's turn
        if action == 'Pass':
            self.passCount += 1
            self.UpdateGameStateVariables()
            return self

        actionX, actionY = action

        # Update the board and the stoneGroups with the current player's move
        self.stoneGroups[action] = {action}
        self.board[actionX][actionY] = self.turn

        # Merge the new stone with neighboring stones
        self.MergeNeighboringStones(action, self.stoneGroups, self.board)

        # Check whether any of the opponent's stones should flip
        checkedOpposite = 5 * [5 * [False]]  # keeping track of whether opponent stone is already checked (for faster performance)
        for stone in self.stoneGroups[action]:  # Check all stones in the new group
            stoneX, stoneY = stone
            # Search for any neighboring opponent's stones
            for x in range(stoneX - 1, stoneX + 2):
                for y in range(stoneY - 1, stoneY + 2):
                    # Ignore diagonals
                    if (abs(x - stoneX) + abs(y - stoneY)) is not 1:
                        continue
                    # Make sure neighbor is on the board
                    elif x < 0 or x > 4 or y < 0 or y > 4:
                        continue
                    # Ignore empty places
                    elif self.board[x][y] is None:
                        continue
                    # Ignore opponent's stones that were already checked
                    elif checkedOpposite[x][y] == True:
                        continue
                    # Found an unchecked opponent's stone!
                    elif self.board[x][y] is not self.turn:
                        # Is the opponent's stone's group trapped? Can replace with ours then!
                        if self.IsGroupTrapped(self.stoneGroups, self.board, (x, y)):
                            self.MergeGroups(self.stoneGroups, (x, y), stone)  # Merge opponent's group with ours
                            # Change the color of their stones to ours
                            for oppStone in self.stoneGroups[(x, y)]:
                                oppStoneX, oppStoneY = oppStone
                                self.board[oppStoneX][oppStoneY] = self.turn
                                # If the opponent's group had any neighboring stones that were ours, merge those into a single group as well
                                for oppX in range(oppStoneX - 1, oppStoneX + 2):
                                    for oppY in range(oppStoneY - 1, oppStoneY + 2):
                                        # Ignore diagonals
                                        if (abs(oppX - oppStoneX) + abs(oppY - oppStoneY)) is not 1:
                                            continue
                                        # Make sure location is on the board
                                        if oppX < 0 or oppX > 4 or oppY < 0 or oppY > 4:
                                            continue
                                        # If the stone is our's merge that stone's group with our 'trapping' group
                                        if self.board[oppX][oppY] is self.turn:
                                            self.MergeGroups(self.stoneGroups, (oppX, oppY), stone)
                        # Keep track off all the opponent's stones we've already visited, so we don't have to revisit them again (faster performance)
                        for oppStone in self.stoneGroups[(x, y)]:
                            oppStoneX, oppStoneY = oppStone
                            checkedOpposite[oppStoneX][oppStoneY] = True
        # Turn is complete, update the game state
        self.UpdateGameStateVariables()
        return self

    def UpdateGameStateVariables(self):
        """Updates the game state variables after a turn is complete.
        This includes:
            Count of black and white stones on the board
            Whose turn it is

        inputs:
            None
        returns:
            None
        """
        # Update stone count
        self.numBlack = 0
        self.numWhite = 0
        for row in self.board:
            for stone in row:
                if stone == 'B':
                    self.numBlack += 1
                elif stone == 'W':
                    self.numWhite += 1
        # Update whose turn it is
        if self.turn == 'B':
            self.turn = 'W'
        else:
            self.turn = 'B'


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
            stoneX, stoneY = stone
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

        actionX, actionY = action

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
        actionX, actionY = action

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
