def MiniMaxDecision(state):
    """Decides what action to do that will maximize the minimax value

    inputs:
        (State)state: Current State
    returns:
        (State)maxAction: Action that leaves the State in the best condition for maximizing minimax value
    """
    maxAction = None
    maxMinValue = float("-inf")
    for action in state.GetActions():
        actionMaxMinValue = MinValue(state.Result(action))
        if actionMaxMinValue > maxMinValue:
            maxMinValue = actionMaxMinValue
            maxAction = action
    return maxAction


def MinValue(state):
    """Returns what the minimum minimax value can be for the opponent's turn when the game has terminated

    inputs:
        (State)state: Current State
    returns:
        (int)minValue: minimum value that the the minimax value can be at the end of the game
    """
    if state.TerminalTest():
        return state.Utility()
    minValue = float("inf")
    for action in state.GetActions():
        minValue = min(MaxValue(state.Result(action)), minValue)
    return minValue


def MaxValue(state):
    """Returns what the maximum minimax value can be for the opponent's turn when the game has terminated

    inputs:
        (State)state: Current State
    returns:
        (int)minValue: maximum value that the the minimax value can be at the end of the game
    """
    if state.TerminalTest():
        return state.Utility()
    maxValue = float("-inf")
    for action in state.GetActions():
        maxValue = max(MinValue(state.Result(action)), maxValue)
    return maxValue
