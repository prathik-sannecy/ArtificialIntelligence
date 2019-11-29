def MiniMaxDecision(state):
    maxAction = None
    maxMinValue = float("-inf")
    for action in state.GetActions():
        actionMaxMinValue = MinValue(state.Result(action))
        if actionMaxMinValue > maxMinValue:
            maxMinValue = actionMaxMinValue
            maxAction = action
    return maxAction

def MinValue(state):
    if state.TerminalTest():
        return state.Utility()
    minValue = float("inf")
    for action in state.GetActions():
        minValue = min(MaxValue(state.Result(action)), minValue)
    return minValue

def MaxValue(state):
    if state.TerminalTest():
        return state.Utility()
    maxValue = float("-inf")
    for action in state.GetActions():
        maxValue = max(MinValue(state.Result(action)), maxValue)
    return maxValue

