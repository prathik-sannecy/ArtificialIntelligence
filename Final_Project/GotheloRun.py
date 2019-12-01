#!/usr/bin/python3

# Random-move Gothello player.
# Leveraged from:
# https://github.com/pdx-cs-ai/gothello-libclient-python3

import random
import sys

import Final_Project.gthclient as gthclient
import Final_Project.GameState as GameState
import Final_Project.MiniMax as MiniMax

me = sys.argv[1]
opp = gthclient.opponent(me)

client = gthclient.GthClient(me, "localhost", 0)

depthSearch = 3

def letter_range(letter):
    for i in range(5):
        yield chr(ord(letter) + i)

board = {letter + digit
         for letter in letter_range('a')
         for digit in letter_range('1')}

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
gameState = GameState.GameState()

def IndexPosToStrPos(indexPos):
    if indexPos == 'pass':
        return 'pass'
    numToLet = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
    return numToLet[indexPos[1]] + str(5 - indexPos[0])

def StrPosToIndexPos(strPos):
    if strPos == 'pass':
        return 'pass'
    letToNum = {'a': 4, 'b': 3, 'c': 2, 'd': 1, 'e': 0}
    x = 4 - int(strPos[1]) + 1
    y = 4 - letToNum[strPos[0]]
    return (x, y)

while True:
    show_position()
    if side == me:
        move = MiniMax.MiniMaxDecision(gameState, depthSearch)
        gameState.Result(move)
        print(move)
        print("me:", move, IndexPosToStrPos(move))
        print(gameState.board)
        move = IndexPosToStrPos(move)
        try:
            client.make_move(move)
            # grid[me].add(move)
            # board.remove(move)
        except gthclient.MoveError as e:
            if e.cause == e.ILLEGAL:
                print("me: made illegal move, passing")
                client.make_move("pass")
    else:
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
            print(gameState.board)

    side = gthclient.opponent(side)
