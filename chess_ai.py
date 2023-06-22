from chess_ui import *
import random

board1 = createBoard()
boardUI(board1)

def makeMove(board: dict, turn: Turn, str_move: str):                # Executes the move and changes the turn. Returns the board and turn as a tuple.

    move = str_move.split("-")

    turn.moveMade(board[move[0]], move[1])

    board[move[1]] = board[move[0]]
    board[move[0]] = None
    board[move[1]].MOVED()

    return board, turn

starting_player = Turn("white")

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

def searchMoves(moves, depth, turn, board):

    if not depth:

        return

    for move in moves:

        board_copy = board.copy()

        makeMove(board_copy, turn, move)

        future_moves = checklegal(turn.Turn(), board_copy, "string_move", None)

        if turn == "white":

            turn = "black"

        else:

            turn = "white"

        searchMoves(future_moves, depth - 1, turn, board_copy)

        if turn == "white":

            turn = "black"

        else:

            turn = "white"

def findMove(moves, turn, board):

    eval_table = searchMoves(moves, 2, turn, board)


def test(turn: Turn, board: createBoard):
    print()

    legal_moves = checklegal(turn.Turn(), board, "string_move", None)

    if turn.Turn() == "black":

        move = findMove(legal_moves, turn, board)        

        info = makeMove(board, turn, move)
        
        board = info[0]
        turn = info[1]

        boardUI(board)

    else:

        player_move = input()

        if player_move in legal_moves:

            info = makeMove(board, turn, player_move)
            board = info[0]
            turn = info[1]
            boardUI(board)
        
        else:

            print("Invalid move.")

while True:

    test(starting_player, board1)
