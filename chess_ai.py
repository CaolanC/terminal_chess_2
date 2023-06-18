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

a = Turn("black")

def test(turn: Turn, board: createBoard):
    print()

    legal_moves = checklegal(turn.Turn(), board, "string_move", None)

    if turn.Turn() == "black":
        random_move = random.choice(legal_moves)

        info = makeMove(board, turn, random_move)
        
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

    test(a, board1)
