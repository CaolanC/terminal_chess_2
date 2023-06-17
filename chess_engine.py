# Required Classes

from chess_ui import LegalMove
from chess_ui import Turn
from chess_ui import enPassantableSquareObject
from chess_ui import Piece

# Required Functions

from chess_ui import checklegal
from chess_ui import createBoard
from chess_ui import boardUI

# Testing Functions

from os import system
from time import sleep

# Engine

# Testing

board = createBoard()
turnTracker = Turn()
enpSQ = None

boardUI(board)


def doMove(mv, board):
    board = board.copy()
    board[mv.destination()] = board[mv.origin()]
    board[mv.origin()] = None

    return board

global positions

positions = 0

def engine(mvs, board, turn, depth):

    global positions

    board = board.copy()

    if not depth:

        positions += 1
        return True

    else:

        for mv in mvs:

            new_B = doMove(mv, board)

            # boardUI(new_B)
            # print(mv.origin(), mv.destination())    
            # print(depth)


            # system("clear")

            if turn == "white":

                turn = "black"
            
            else:

                turn = "white"

            engine(checklegal(turn, new_B, "object_move", enpSQ), new_B, turn, depth - 1)

            if turn == "white":

                turn = "black"
            
            else:

                turn = "white"
        print(positions)

engine(checklegal(turnTracker.Turn(), board, "object_move", enpSQ), board, turnTracker.Turn(), 3)