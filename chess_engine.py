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

sudo_centre = ["e4", "e5", "d4", "d5"]
inf_centre = ["e3", "e6", "d3", "d6", "c3", "c4", "c5", "c6", "f3", "f4", "f5", "f6"]

global positions

positions = 0

def eval(board):
    w_score = 0
    b_score = 0

    for piece in board:

        if board[piece]:

            if board[piece].COL() == "white":
                if board[piece].PC() == "pawn":
                    w_score += 1
                    w_score += (int(piece[1]) / 7)

                elif board[piece].PC() == "queen":
                    w_score += 9
                    
                elif board[piece].PC() == "bishop":
                    w_score += 3
                    
                elif board[piece].PC() == "rook":
                    w_score += 4
                    
                elif board[piece].PC() == "knight":
                    w_score += 2.75
                    if piece in sudo_centre:
                        b_score += 0.7
                    elif piece in inf_centre:
                        b_score += 0.3

            if board[piece].COL() == "black":

                if board[piece].PC() == "pawn":
                    b_score += 1
                    b_score += (((int(piece[1]) * - 1) + 9) / 7)

                elif board[piece].PC() == "queen":
                    b_score += 9
                    
                elif board[piece].PC() == "bishop":
                    b_score += 3
                    
                elif board[piece].PC() == "rook":
                    b_score += 4
                    
                elif board[piece].PC() == "knight":
                    b_score += 2.75
                    if piece in sudo_centre:
                        b_score += 0.7
                    elif piece in inf_centre:
                        b_score += 0.3

    return w_score - b_score         

        
# print(eval(board))

def engine(mvs, board, turn, depth):

    global positions

    board = board.copy()

    if not depth:

        positions += 1
        a = (eval(board))
        print(eval(board))
        return a

    else:

        for mv in mvs:

                new_B = doMove(mv, board)

                print(mv.origin(), mv.destination())    
                # print(positions)

                # system("clear")
            
                # boardUI(new_B)
                # input()

                if turn == "white":

                    turn = "black"
            
                else:

                    turn = "white"

                SCORE = engine(checklegal(turn, new_B, "object_move", enpSQ), new_B, turn, depth - 1)
                if turn == "white":

                    turn = "black"
            
                else:

                    turn = "white"
        print(positions)

engine(checklegal(turnTracker.Turn(), board, "object_move", enpSQ), board, turnTracker.Turn(), 3)