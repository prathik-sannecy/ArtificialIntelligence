#!/usr/bin/python3

# Gothello player using depth limited search.
# Leveraged from:
# https://github.com/pdx-cs-ai/gothello-libclient-python3

import random
import sys

import gthclient
import GameState
import MiniMax

me = sys.argv[1]
opp = gthclient.opponent(me)

client = gthclient.GthClient(me, "localhost", 0)

depthSearch = 3

def letter_range(letter):
    for i in range(5):
        yield chr(ord(letter) + i)

grid = {"white": set(), "black": set()}

def show_position():
    for digit in letter_range('1'):
        for letter in letter_range('a'):
            pos = letter + digit
            if pos in grid["white"]:
                piece = "O"
            elif pos in grid["black"]:
                piece = "*"
            else:
                piece = "."
            print(piece, end="")
        print()

side = "black"
gameState = GameState.GameState(me)

def IndexPosToStrPos(indexPos):
    """Translate a move from my format to server's side's format"""
    if indexPos == 'pass':
        return 'pass'
    numToLet = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
    return numToLet[indexPos[1]] + str(5 - indexPos[0])

def StrPosToIndexPos(strPos):
    """Translate a move from client's side format to my format"""
    if strPos == 'pass':
        return 'pass'
    letToNum = {'a': 4, 'b': 3, 'c': 2, 'd': 1, 'e': 0}
    x = 4 - int(strPos[1]) + 1
    y = 4 - letToNum[strPos[0]]
    return (x, y)

while True:
    show_position()
    if side == me:  # my turn
        move = MiniMax.MiniMaxDecision(gameState, depthSearch)  # find the best move
        gameState.Result(move)  # do the best move
        print("me:", move, IndexPosToStrPos(move))
        move = IndexPosToStrPos(move)  # translate the move from my format to the server's format
        try:
            client.make_move(move)
        except gthclient.MoveError as e:
            if e.cause == e.ILLEGAL:
                print("me: made illegal move, passing")
                client.make_move("pass")
    else:  # opponent's turn
        cont, move = client.get_move()
        print("opp:", move)
        if cont and move == "pass":
            print("me: pass to end game")
            client.make_move("pass")
            break
        else:
            if not cont:
                break
            gameState = gameState.Result(StrPosToIndexPos(move))

    side = gthclient.opponent(side)
