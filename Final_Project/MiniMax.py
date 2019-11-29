def MiniMaxDecision(state):
    maxAction = None
    maxMinValue = float("-inf")
    for action in state.actions:
        actionMaxMinValue = MinValue(action)
        if actionMaxMinValue > maxMinValue:
            maxMinValue = actionMaxMinValue
            maxAction = action
    return maxAction

def MinValue(state):
    if state.TerminalTest():
        return state.utility
    minValue = float("inf")
    for action in state.actions:
        minValue = min(MaxValue(action), minValue)
    return minValue

def MaxValue(state):
    if state.TerminalTest():
        return state.utility
    maxValue = float("-inf")
    for action in state.actions:
        maxValue = min(MinValue(action), maxValue)
    return maxValue

