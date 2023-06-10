class Turn(object):

    def __init__(self):
        
        self.player = "white"
        self.wKingPos = "e1"
        self.bKingPos = "e8"
    
    def Turn(self):
        
        return self.player
    
    def moveMade(self, PC, b):

        if PC.piece() == "king":
            if PC.color == "white":

                self.wKingPos = b
            
            elif PC.color == "black":

                self.bKingPos = b

        if self.player ==  "white":
            self.player = "black"
        else:
            self.player = "white"

    def WKpos(self):

        return self.wKingPos
    
    def BKpos(self):

        return self.bKingPos

class Piece(object):

    def __init__(self, color, piece, square, moved, symbol):

        self.color = color
        self.piece = piece
        self.square = square
        self.moved = moved
        self.symbol = symbol

    def SYM(self):

        return self.symbol

    def COL(self):

        return self.color

    def PC(self):

        return self.piece

    def SQ(self):

        return self.square

    def hasMoved(self):

        return self.moved

    def MOVED(self):

        self.moved = True


def createBoard():
    board = {}
    for number in range(8):
        for letter in range(8):
            board[str(chr(letter + 97)) + str(number + 1)] = None

    board["a1"] = Piece("white", "rook", "a1", False, "\033[37m \u265c")
    board["b1"] = Piece("white", "knight", "b1", False, "\033[37m \u265e")
    board["c1"] = Piece("white", "bishop", "c1", False, "\033[37m \u265d")
    board["d1"] = Piece("white", "queen", "d1", False, "\033[37m \u265b")
    board["e1"] = Piece("white", "king", "e1", False, "\033[37m \u265a")
    board["f1"] = Piece("white", "bishop", "f1", False, "\033[37m \u265d")
    board["g1"] = Piece("white", "knight", "g1", False, "\033[37m \u265e")
    board["h1"] = Piece("white", "rook", "h1", False, "\033[37m \u265c")

    board["a2"] = Piece("white", "pawn", "a2", False, "\033[37m \u265F\033[37m")
    board["b2"] = Piece("white", "pawn", "b2", False, "\033[37m \u265F\033[37m")
    board["c2"] = Piece("white", "pawn", "c2", False, "\033[37m \u265F\033[37m")
    board["d2"] = Piece("white", "pawn", "d2", False, "\033[37m \u265F\033[37m")
    board["e2"] = Piece("white", "pawn", "e2", False, "\033[37m \u265F\033[37m")
    board["f2"] = Piece("white", "pawn", "f2", False, "\033[37m \u265F\033[37m")
    board["g2"] = Piece("white", "pawn", "g2", False, "\033[37m \u265F\033[37m")
    board["h2"] = Piece("white", "pawn", "h2", False, "\033[37m \u265F\033[37m")

    board["a8"] = Piece("black", "rook", "a8", False, "\033[30m \u265c")
    board["b8"] = Piece("black", "knight", "b8", False, "\033[30m \u265e")
    board["c8"] = Piece("black", "bishop", "c8", False, "\033[30m \u265d")
    board["d8"] = Piece("black", "queen", "d8", False, "\033[30m \u265b")
    board["e8"] = Piece("black", "king", "e8", False, "\033[30m \u265b")
    board["f8"] = Piece("black", "bishop", "f8", False, "\033[30m \u265d")
    board["g8"] = Piece("black", "knight", "g8", False, "\033[30m \u265e")
    board["h8"] = Piece("black", "rook", "h8", False, "\033[30m \u265c")

    board["a7"] = Piece("black", "pawn", "a7", False, "\033[30m \u265F")
    board["b7"] = Piece("black", "pawn", "b7", False, "\033[30m \u265F")
    board["c7"] = Piece("black", "pawn", "c7", False, "\033[30m \u265F")
    board["d7"] = Piece("black", "pawn", "d7", False, "\033[30m \u265F")
    board["e7"] = Piece("black", "pawn", "e7", False, "\033[30m \u265F")
    board["f7"] = Piece("black", "pawn", "f7", False, "\033[30m \u265F")
    board["g7"] = Piece("black", "pawn", "g7", False, "\033[30m \u265F")
    board["h7"] = Piece("black", "pawn", "h7", False, "\033[30m \u265F")
  
    return board

def boardUI(board):
    bg_color = 0
    for number in range(7, -1, -1):
        row = ""
        for letter in range(8):
            if bg_color % 2 == 0:
                row += "\033[42m"
            else:
                row += "\033[45m"
            piece = board[str(chr(letter + 97)) + str(number + 1)]
            if piece:
                row += piece.SYM()
            else:
                row += "  "
            bg_color += 1
        bg_color += 1
        row += "\033[40m"
        print(row)

def startGame():
    board = createBoard()
    turnTracker = Turn()
    boardUI(board)
    while True:
        move = input()
        parsedMoves = parseMove(move)
        if parsedMoves[0] in board and parsedMoves[1] in board and legalMove(parsedMoves, board, turnTracker):
            board[parsedMoves[1]] = board[parsedMoves[0]]
            board[parsedMoves[0]] = None
            turnTracker.moveMade()
            boardUI(board)       


def parseMove(move):
    move = move.split("-")
    a = move[0]
    b = move[1]
    return [a, b]

def legalMove(moves, board, turnTracker):
    a = moves[0]
    b = moves[1]

    if isTurn(a, board, turnTracker) and possibleMove(a, b, board, turnTracker):
        return True
    else:
        return False

def isTurn(piece, board, turnTracker):
    
    if turnTracker.Turn() == board[piece].COL():
        return True
    else:
        return False

def possibleMove(a, b, board, turnTracker):
    aPosPiece = board[a].PC()
    aColPiece = board[a].COL()
    bColPiece = board[b].COL()

    inCheck = putsSidesKingInCheck(a, b, turnTracker, board)

    match aPosPiece:

        case "pawn":

            pass

def putsSidesKingInCheck(a, b, turnTracker, board):
    
    tempBoard = board

    tempBoard[b] = tempBoard[a]
    tempBoard[a] =  None

    if turnTracker.Turn() == "white":

        pass
    
    else:

        pass

    return False

startGame()