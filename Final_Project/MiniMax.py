from copy import deepcopy

def MiniMaxDecision(state, maxDepth = float('inf')):
    """Decides what action to do that will maximize the minimax value

    inputs:
        (State)state: Current State
    returns:
        (State)maxAction: Action that leaves the State in the best condition for maximizing minimax value
    """
    maxAction = None
    maxMinValue = float("-inf")
    for action in state.GetActions():
        localCopyState = deepcopy(state)
        actionMaxMinValue = MinValue(localCopyState.Result(action), maxDepth, 0)
        if actionMaxMinValue > maxMinValue:
            maxMinValue = actionMaxMinValue
            maxAction = action
        # Give preference to center squares
        elif actionMaxMinValue == maxMinValue:
            if (abs(action[0] - 2) + abs(action[1] - 2)) < (abs(maxAction[0] - 2) + abs(maxAction[1] - 2)):
                maxAction = action

    return maxAction


def MinValue(state, maxDepth = float('inf'), depthCount = 0):
    """Returns what the minimum minimax value can be for the opponent's turn when the game has terminated

    inputs:
        (State)state: Current State
    returns:
        (int)minValue: minimum value that the the minimax value can be at the end of the game
    """
    depthCount += 1
    if state.TerminalTest() or (depthCount == maxDepth):
        return state.Utility()
    minValue = float("inf")
    for action in state.GetActions():
        localCopyState = deepcopy(state)
        minValue = min(MaxValue(localCopyState.Result(action), maxDepth, depthCount), minValue)
    return minValue


def MaxValue(state, maxDepth = float('inf'), depthCount = 0):
    """Returns what the maximum minimax value can be for the opponent's turn when the game has terminated

    inputs:
        (State)state: Current State
    returns:
        (int)minValue: maximum value that the the minimax value can be at the end of the game
    """
    depthCount += 1
    if state.TerminalTest() or (depthCount == maxDepth):
        return state.Utility()
    maxValue = float("-inf")
    for action in state.GetActions():
        localCopyState = deepcopy(state)
        maxValue = max(MinValue(localCopyState.Result(action), maxDepth, depthCount), maxValue)
    return maxValue
