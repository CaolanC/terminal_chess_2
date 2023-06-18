from chess_ui import *
import random

board1 = createBoard()
boardUI(board1)


a = Turn("black")

def test(turn: Turn, board: createBoard):    
    if turn.player == "black":
        legal_moves = checklegal("black", board, "string_move", None)
        print(legal_moves)
        random_move = random.choice(legal_moves)
        half = random_move.split("-")
        print(half)
        turn.moveMade(board[half[0]], half[1])
        board[half[1]] = board[half[0]]
        board[half[0]] = None
        board[half[1]].MOVED()
        
        boardUI(board)
    else:
        b = input()
        c = b.split("-")
        print(c)

while True:

    test(a, board1)
