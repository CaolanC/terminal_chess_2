# Global Variables

class enPassantableSquareObject(object):

    def __init__(self, square, color):

        self.square = square
        self.color = color
    
    def enSquare(self):

        return self.square
    
    def enColor(self):

        return self.color
    
    def __bool__(self):

        return True

class LegalMove(object):

    def __init__(self, origin, destination):

        self.orgn = origin
        self.dest = destination

    def origin(self):
        
        return self.orgn

    def destination(self):

        return self.dest
    
    def __str__(self):

        return self.orgn + '-' + self.dest

class Turn(object):

    def __init__(self, player="white", wking="e1", bking="e8"):
        
        self.player = player
        self.wKingPos = wking
        self.bKingPos = bking
    
    def Turn(self):
        
        return self.player
    
    def moveMade(self, a, b):

        if a.PC() == "king":
            if a.COL() == "white":

                self.wKingPos = b
            
            elif a.COL() == "black":

                self.bKingPos = b

        if self.player ==  "white":
            self.player = "black"
        else:
            self.player = "white"

    def WKpos(self):

        return self.wKingPos
    
    def BKpos(self):

        return self.bKingPos
    
    def invert(self):

        if self.player == "white":
            self.player = "black"
        else:
            self.player = "white"

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

    board["a1"] = Piece("white", "rook", "a1", False,   "\033[37m\u265c ")
    board["b1"] = Piece("white", "knight", "b1", False, "\033[37m\u265e ")
    board["c1"] = Piece("white", "bishop", "c1", False, "\033[37m\u265d ")
    board["d1"] = Piece("white", "queen", "d1", False,  "\033[37m\u265b ")
    board["e1"] = Piece("white", "king", "e1", False,   "\033[37m\u265a ")
    board["f1"] = Piece("white", "bishop", "f1", False, "\033[37m\u265d ")
    board["g1"] = Piece("white", "knight", "g1", False, "\033[37m\u265e ")
    board["h1"] = Piece("white", "rook", "h1", False,   "\033[37m\u265c ")

    board["a2"] = Piece("white", "pawn", "a2", False, "\033[37m\u2659 ")
    board["b2"] = Piece("white", "pawn", "b2", False, "\033[37m\u2659 ")
    board["c2"] = Piece("white", "pawn", "c2", False, "\033[37m\u2659 ")
    board["d2"] = Piece("white", "pawn", "d2", False, "\033[37m\u2659 ")
    board["e2"] = Piece("white", "pawn", "e2", False, "\033[37m\u2659 ")
    board["f2"] = Piece("white", "pawn", "f2", False, "\033[37m\u2659 ")
    board["g2"] = Piece("white", "pawn", "g2", False, "\033[37m\u2659 ")
    board["h2"] = Piece("white", "pawn", "h2", False, "\033[37m\u2659 ")

    board["a8"] = Piece("black", "rook", "a8", False,   "\033[30m\u265c ")
    board["b8"] = Piece("black", "knight", "b8", False, "\033[30m\u265e ")
    board["c8"] = Piece("black", "bishop", "c8", False, "\033[30m\u265d ")
    board["d8"] = Piece("black", "queen", "d8", False,  "\033[30m\u265b ")
    board["e8"] = Piece("black", "king", "e8", False,   "\033[30m\u265a ")
    board["f8"] = Piece("black", "bishop", "f8", False, "\033[30m\u265d ")
    board["g8"] = Piece("black", "knight", "g8", False, "\033[30m\u265e ")
    board["h8"] = Piece("black", "rook", "h8", False,   "\033[30m\u265c ")

    board["a7"] = Piece("black", "pawn", "a7", False, "\033[30m\u265F ")
    board["b7"] = Piece("black", "pawn", "b7", False, "\033[30m\u265F ")
    board["c7"] = Piece("black", "pawn", "c7", False, "\033[30m\u265F ")
    board["d7"] = Piece("black", "pawn", "d7", False, "\033[30m\u265F ")
    board["e7"] = Piece("black", "pawn", "e7", False, "\033[30m\u265F ")
    board["f7"] = Piece("black", "pawn", "f7", False, "\033[30m\u265F ")
    board["g7"] = Piece("black", "pawn", "g7", False, "\033[30m\u265F ")
    board["h7"] = Piece("black", "pawn", "h7", False, "\033[30m\u265F ")

    return board

def boardUI(board):
    bg_color = 0
    for number in range(7, -1, -1):
        row = ""
        for letter in range(8):
            if bg_color % 2 == 0:
                row += "\033[44m"
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

    
    enpSQ = None


    while True:


        legal_moves = checklegal(turnTracker.Turn(), board, "string_move", enpSQ)
        if checkmate(legal_moves, board, turnTracker):

            if turnTracker.Turn() == "white":

                winner = "Black"

            else:

                winner = "White"

            print("Checkmate! " + winner + " wins!")

        move = input()
        parsedMoves = parseMove(move)

        if parsedMoves[0] in board and parsedMoves[1] in board and legalMove(parsedMoves, board, turnTracker) and move in checklegal(turnTracker.Turn(), board, "string_move", enpSQ):

            if enpSQ:
                if board[parsedMoves[0]].PC() == "pawn":
                    if turnTracker.Turn() == "white" and parsedMoves[1] == enpSQ.enSquare():
                        LE = parsedMoves[1][0]
                        NU = parsedMoves[1][1]
                        board[LE + str(int(NU) - 1)] = None

                    elif turnTracker.Turn() == "black" and parsedMoves[1] == enpSQ.enSquare():
                        LE = parsedMoves[1][0]
                        NU = parsedMoves[1][1]
                        board[LE + str(int(NU) + 1)] = None

            if not board[parsedMoves[0]].hasMoved():
                if board[parsedMoves[0]].PC() == "pawn":
                    enpSQ = genEnPassentSquare(parsedMoves[0], turnTracker.Turn(), parsedMoves[1], board)
            else:
                enpSQ = None

            turnTracker.moveMade(board[parsedMoves[0]], board[parsedMoves[1]])

            board[parsedMoves[0]].MOVED()
            board[parsedMoves[1]] = board[parsedMoves[0]]
            board[parsedMoves[0]] = None
            boardUI(board)

        elif move == "O-O" or move == "0-0":
            if not inCheck(turnTracker, board):
                if turnTracker.Turn() == "white":
                    if not inCheck(turnTracker, board, "f1") and not inCheck(turnTracker, board, "g1"):
                        if not board["f1"] and not board["g1"] and board["h1"].PC() == "rook" and board["h1"].COL() == turnTracker.Turn() and not board["h1"].hasMoved():

                            turnTracker.moveMade(board["e1"], "g1")

                            board["g1"] = board["e1"]
                            board["e1"] = None
                            board["f1"] = board["h1"]
                            board["h1"] = None

                            board["g1"].MOVED()
                            board["f1"].MOVED()
                            boardUI(board)
                elif turnTracker.Turn() == "black":
                    if not inCheck(turnTracker, board, "f8") and not inCheck(turnTracker, board, "g8"):
                        if not board["f8"] and not board["g8"] and board["h8"].PC() == "rook" and board["h8"].COL() == turnTracker.Turn() and not board["h8"].hasMoved():

                            turnTracker.moveMade(board["e8"], "g8")

                            board["g8"] = board["e8"]
                            board["e8"] = None
                            board["f8"] = board["h8"]
                            board["h8"] = None

                            board["g8"].MOVED()
                            board["f8"].MOVED()
                            boardUI(board)


        elif move == "O-O-O" or move == "0-0-0":

            if not inCheck(turnTracker, board):
                if turnTracker.Turn() == "white":
                    if not inCheck(turnTracker, board, "d1") and not inCheck(turnTracker, board, "c1"):
                        if not board["d1"] and not board["c1"] and board["a1"].PC() == "rook" and board["a1"].COL() == turnTracker.Turn() and not board["a1"].hasMoved():

                            turnTracker.moveMade(board["e1"], "c1")

                            board["c1"] = board["e1"]
                            board["e1"] = None
                            board["d1"] = board["a1"]
                            board["a1"] = None

                            board["c1"].MOVED()
                            board["d1"].MOVED()
                            boardUI(board)
                elif turnTracker.Turn() == "black":
                    if not inCheck(turnTracker, board, "d8") and not inCheck(turnTracker, board, "c8"):
                        if not board["d8"] and not board["c8"] and board["a8"].PC() == "rook" and board["a8"].COL() == turnTracker.Turn() and not board["a8"].hasMoved():

                            turnTracker.moveMade(board["e8"], "c8")

                            board["c8"] = board["e8"]
                            board["e8"] = None
                            board["d8"] = board["a8"]
                            board["a8"] = None

                            board["c8"].MOVED()
                            board["d8"].MOVED()
                            boardUI(board)

def checkmate(moves, board, turn):

    for move in moves:
        if legalMove(parseMove(move), board, turn):
            return False
        
    return True
            
def inCheck(turnTracker, board, position=None):
    
    tempBoard = board.copy()
    tempTurnTracker = Turn(turnTracker.Turn(), turnTracker.WKpos(), turnTracker.BKpos())

    if not position and tempTurnTracker.Turn() == "black":

        King = tempTurnTracker.BKpos()
        KingL = King[0]
        KingN = King[1]

    elif not position:

        King = tempTurnTracker.WKpos()
        KingL = King[0]
        KingN = King[1]

    else:

        KingL = position[0]
        KingN = position[1]

    N = nAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())
    RQ = rqAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())
    P = pAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())
    BQ = bqAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())
    K = kAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())

    if not N and not RQ and not P and not BQ and not K:
        return False
    else:
        return True

def genEnPassentSquare(pc, turn, dest, board):

    if turn == "white" and dest == pc[0] + str(int(pc[1]) + 2):

        return enPassantableSquareObject(pc[0] + str(int(pc[1]) + 1), turn)
    
    if turn == "black" and dest == pc[0] + str(int(pc[1]) - 2):

        return enPassantableSquareObject(pc[0] + str(int(pc[1]) - 1), turn)

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

    if board[a]:

        aColPiece = board[a].COL()
        aPosPiece = board[a].PC()

    if board[b]:

        bColPiece = board[b].COL()
        bPosPiece = board[b].PC()

    inCheck = putsSidesKingInCheck(a, b, turnTracker, board)

    if not inCheck:

        return True

    else:

        return False

def putsSidesKingInCheck(a, b, turnTracker, board):
    
    tempBoard = board.copy()
    tempTurnTracker = Turn(turnTracker.Turn(), turnTracker.WKpos(), turnTracker.BKpos())
    
    tempTurnTracker.moveMade(tempBoard[a], b)
    tempBoard[b] = tempBoard[a]
    tempBoard[a] =  None

    tempTurnTracker.invert()

    if tempTurnTracker.Turn() == "black":

        King = tempTurnTracker.BKpos()

    else:

        King = tempTurnTracker.WKpos()

    KingL = King[0]
    KingN = King[1]

    N = nAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())
    RQ = rqAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())
    P = pAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())
    BQ = bqAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())
    K = kAttacking(KingL, KingN, tempBoard, tempTurnTracker.Turn())

    if not N and not RQ and not P and not BQ and not K:
        return False
    else:
        return True
    
def kAttacking(L, N, board, turn):

    N = int(N)

    uu = L + str(N + 1)
    ur = chr(ord(L) + 1) + str(N + 1)
    ul = chr(ord(L) - 1) + str(N + 1)
    rr = chr(ord(L) + 1) + str(N)
    ll = chr(ord(L) - 1) + str(N)
    dd = L + str(N - 1)
    dr = chr(ord(L) + 1) + str(N - 1)
    dl = chr(ord(L) - 1) + str(N - 1)

    coords = [uu, ur, ul, rr, ll, dd, dr, dl]

    for co in coords:
        if co in board and board[co]:
            if board[co].PC() == "king" and board[co].COL() != turn:
               return True
    return False

def pAttacking(L, N, board, turn):

    N = int(N)
    if turn == "white":
        leftP = chr(ord(L) - 1) + str(N + 1)
        rightP = chr(ord(L) + 1) + str(N + 1)

    elif turn == "black":
        leftP = chr(ord(L) - 1) + str(N - 1)
        rightP = chr(ord(L) + 1) + str(N - 1)

    if turn == "white":
        if leftP in board and board[leftP] and board[leftP].PC() == "pawn" and board[leftP].COL() != "white":
            return True
        if rightP in board and board[rightP] and board[rightP].PC() == "pawn" and board[rightP].COL() != "white":
            return True
    else:
        if leftP in board and board[leftP] and board[leftP].PC() == "pawn" and board[leftP].COL() != "black":
            return True
        if rightP in board and board[rightP] and board[rightP].PC() == "pawn" and board[rightP].COL() != "black":
            return True
        
    return False

def bqAttacking(L, N, board, turn):

    posPos = []

    N = int(N)

    inCheck = False

    # UP RIGHT

    Aletters = [chr(i) for i in range(ord(L) + 1, ord("i"))]
    for i in range(len(Aletters)):
        if N + i + 1 <= 8:
            if board[Aletters[i] + str(N + i + 1)]:
                co = board[Aletters[i] + str(N + i + 1)]
                if co.COL() != turn and (co.PC() == "bishop" or co.PC() == "queen"):
                    return True
                else:
                    break

    #UP LEFT

    Bletters = [chr(i) for i in range(ord("a"), ord(L))]

    for i in range(len(Bletters)):
        if N + i + 1 <= 8:
            if board[Bletters[::-1][i] + str(N + i + 1)]:
                co = board[Bletters[::-1][i] + str(N + i + 1)]
                if co.COL() != turn and (co.PC() == "bishop" or co.PC() == "queen"):
                    return True
                else:
                    break

    for i in range(len(Aletters)):
        if N - i - 1 >= 1:
            if board[Aletters[i] + str(N - i - 1)]:
                co = board[Aletters[i] + str(N - i - 1)]
                if co.COL() != turn and (co.PC() == "bishop" or co.PC() == "queen"):
                    return True
                else:
                    break

    for i in range(len(Bletters)):
        if N - i - 1 >= 1:
            if board[Bletters[::-1][i] + str(N - i - 1)]:
                co = board[Bletters[::-1][i] + str(N - i - 1)]
                if co.COL() != turn and (co.PC() == "bishop" or co.PC() == "queen"):
                    return True
                else:
                    break

    return False

def rqAttacking(L, N, board, turn):

    posPos = []

    N = int(N)

    inCheck = False

    for i in range(N + 1, 9):
        co = L + str(i)
        if board[co]:
            if board[co].COL() != turn and (board[co].PC() == "rook" or board[co].PC() == "queen"):
                return True
            
            elif board[co]:
                break
            
    for i in range(N - 1, 0, -1):
        co = L + str(i)
        if board[co]:
            if board[co].COL() != turn and (board[co].PC() == "rook" or board[co].PC() == "queen"):
                return True    
            elif board[co]:
                break
            
    for i in range(ord(L) + 1, 105):
        co = chr(i) + str(N)
        if board[co]:
            if board[co].COL() != turn and (board[co].PC() == "rook" or board[co].PC() == "queen"):
                return True
            elif board[co]:
                break
            
    for i in range(ord(L) - 1, 97, -1):
        co = chr(i) + str(N)
        if board[co]:
            if board[co].COL() != turn and (board[co].PC() == "rook" or board[co].PC() == "queen"):
                return True
            elif board[co]:
                break
            
    return False

def nAttacking(L, N, board, turn):

    posPos = []

    N = int(N)

    posPos.append(chr(ord(L) + 1) + str(N - 2))
    posPos.append(chr(ord(L) + 1) + str(N + 2))
    posPos.append(chr(ord(L) + 2) + str(N - 1))
    posPos.append(chr(ord(L) + 2) + str(N + 1))
    posPos.append(chr(ord(L) - 1) + str(N - 2))
    posPos.append(chr(ord(L) - 1) + str(N + 2))
    posPos.append(chr(ord(L) - 2) + str(N - 1))
    posPos.append(chr(ord(L) - 2) + str(N + 1))

    for co in posPos:
        if (len(co) > 2 or int(co[1]) < 1 or int(co[1]) > 8):
            posPos.pop(posPos.index(co))

    for co in posPos:

        if co in board:
            piece = board[co]

            if piece and piece.PC() == "knight" and piece.COL() != turn:

                return True


    return False

def rqMovement(L, N, board, turn):

    rqLegal = []

    N = int(N)

    for i in range(N + 1, 9):
        co = L + str(i)
        if board[co]:
            if board[co].COL() != turn:
                rqLegal.append(LegalMove((L + str(N)), co))
                break

            elif board[co]:
                break
        else:
                rqLegal.append(LegalMove((L + str(N)), co))
            
    for i in range(N - 1, 0, -1):
        co = L + str(i)
        if board[co]:
            if board[co].COL() != turn:
                rqLegal.append(LegalMove((L + str(N)), co))
                break

            elif board[co]:
                break
        else:
                rqLegal.append(LegalMove((L + str(N)), co))
            
    for i in range(ord(L) + 1, 105):
        co = chr(i) + str(N)
        if board[co]:
            if board[co].COL() != turn:
                rqLegal.append(LegalMove((L + str(N)), co))
                break

            elif board[co]:
                break
        else:
                rqLegal.append(LegalMove((L + str(N)), co))
            
    for i in range(ord(L) - 1, 97, -1):
        co = chr(i) + str(N)
        if board[co]:
            if board[co].COL() != turn:
                rqLegal.append(LegalMove((L + str(N)), co))
                break

            elif board[co]:
                break
        else:
                rqLegal.append(LegalMove((L + str(N)), co))

            
    return rqLegal



def nMovement(L, N, board, turn):

    nLegal = []

    posPos = []

    N = int(N)

    posPos.append(chr(ord(L) + 1) + str(N - 2))
    posPos.append(chr(ord(L) + 1) + str(N + 2))
    posPos.append(chr(ord(L) + 2) + str(N - 1))
    posPos.append(chr(ord(L) + 2) + str(N + 1))
    posPos.append(chr(ord(L) - 1) + str(N - 2))
    posPos.append(chr(ord(L) - 1) + str(N + 2))
    posPos.append(chr(ord(L) - 2) + str(N - 1))
    posPos.append(chr(ord(L) - 2) + str(N + 1))

    for co in posPos:

        if co in board:
            piece = board[co]
            if (piece and piece.COL() != turn) or not piece:

                move = LegalMove((L + str(N)), co)
                nLegal.append(move)

    return nLegal

def bqMovement(L, N, board, turn):

    posPos = []

    bqLegal = []

    N = int(N)

    inCheck = False

    # UP RIGHT

    Aletters = [chr(i) for i in range(ord(L) + 1, ord("i"))]
    for i in range(len(Aletters)):
        if N + i + 1 <= 8:
            if Aletters[i] + str(N + i + 1) in board:
                co = Aletters[i] + str(N + i + 1)
                if board[co] and board[co].COL() != turn:
                    bqLegal.append((LegalMove(L + str(N), co)))
                    break
                elif not board[co]:
                    bqLegal.append((LegalMove(L + str(N), co)))

                elif board[co] and board[co].COL() == turn:
                    break                
    #UP LEFT

    Bletters = [chr(i) for i in range(ord("a"), ord(L))]
    
    for i in range(len(Bletters)):
        if N + i + 1 <= 8:
            if Bletters[::-1][i] + str(N + i + 1) in board:
                co = Bletters[::-1][i] + str(N + i + 1)
                if board[co] and board[co].COL() != turn:
                    bqLegal.append((LegalMove(L + str(N), co)))
                    break
                elif not board[co]:
                    bqLegal.append((LegalMove(L + str(N), co)))

                elif board[co] and board[co].COL() == turn:
                    break

    for i in range(len(Aletters)):
        if N - i - 1 >= 1:
            if Aletters[i] + str(N - i - 1) in board:
                co = Aletters[i] + str(N - i - 1)
                if board[co] and board[co].COL() != turn:
                    bqLegal.append((LegalMove(L + str(N), co)))
                    break
                elif not board[co]:
                    bqLegal.append((LegalMove(L + str(N), co)))

                elif board[co] and board[co].COL() == turn:
                    break  

    for i in range(len(Bletters)):
        if N - i - 1 >= 1:
            if Bletters[::-1][i] + str(N - i - 1) in board:
                co = Bletters[::-1][i] + str(N - i - 1)
                if board[co] and board[co].COL() != turn:
                    bqLegal.append((LegalMove(L + str(N), co)))
                    break
                elif not board[co]:
                    bqLegal.append((LegalMove(L + str(N), co)))

                elif board[co] and board[co].COL() == turn:
                    break

    return bqLegal

def kMovement(L, N, board, turn):

    kLegal = []

    N = int(N)

    uu = L + str(N + 1)
    ur = chr(ord(L) + 1) + str(N + 1)
    ul = chr(ord(L) - 1) + str(N + 1)
    rr = chr(ord(L) + 1) + str(N)
    ll = chr(ord(L) - 1) + str(N)
    dd = L + str(N - 1)
    dr = chr(ord(L) + 1) + str(N - 1)
    dl = chr(ord(L) - 1) + str(N - 1)

    coords = [uu, ur, ul, rr, ll, dd, dr, dl]

    for co in coords:
        if co in board and not board[co]:
            kLegal.append(LegalMove(L + str(N), co))
        elif co in board and board[co].COL() != turn:
            kLegal.append(LegalMove(L + str(N), co))

    return kLegal

def pMovement(L, N, board, turn, enpSQ):

    if enpSQ:

        enBool = True

    else:

        enBool = False

    N = int(N)

    pLegal = []

    if turn == "white":
        attackable = [chr(ord(L) + 1) + str(N + 1), chr(ord(L) - 1) + str(N + 1)]
        moveable = [L + str(N + 1)]
        if not board[L + str(N)].hasMoved():
            moveable.append(L + str(N + 2))

    else:
        attackable = [chr(ord(L) + 1) + str(N - 1), chr(ord(L) - 1) + str(N - 1)]
        moveable = [L + str(N - 1)]
        if not board[L + str(N)].hasMoved():
            moveable.append(L + str(N - 2))

    for sq in attackable:

        if sq in board and (board[sq] and board[sq].COL() != turn):
            pLegal.append(LegalMove(L + str(N), sq))

        if (sq in board and not board[sq] and enBool and enpSQ.enColor() != turn and enpSQ.enSquare() == sq):
            pLegal.append(LegalMove(L + str(N), sq))

    for sq in moveable:
        if sq in board and not board[sq]:
            pLegal.append(LegalMove(L + str(N), sq))

    return pLegal

    

def checklegal(turn, board, option, enpSQ):

    legalMoves = []

    for square in board:
        if board[square] and (board[square].PC() == "rook" or board[square].PC() == "queen") and board[square].COL() == turn:
            [legalMoves.append(i) for i in rqMovement(square[0], square[1], board, turn)]

        elif board[square] and board[square].PC() == "knight" and board[square].COL() == turn:
            [legalMoves.append(i) for i in nMovement(square[0], square[1], board, turn)]    
        
        elif board[square] and board[square].PC() == "king" and board[square].COL() == turn:
            [legalMoves.append(i) for i in kMovement(square[0], square[1], board, turn)]

        elif board[square] and board[square].PC() == "pawn" and board[square].COL() == turn:
            [legalMoves.append(i) for i in pMovement(square[0], square[1], board, turn, enpSQ)]

        if board[square] and (board[square].PC() == "bishop" or board[square].PC() == "queen") and board[square].COL() == turn:
            [legalMoves.append(i) for i in bqMovement(square[0], square[1], board, turn)]    

    legalM = []

    if option == "string_move":
        for move in legalMoves:
            legalM.append(str(move))
        return legalM
    
    elif option == "object_move":

        return legalMoves

def test():

    lN = []

    board = createBoard()
    boardUI(board)
    for square in board:
        if board[square] and board[square].PC() == "pawn" and board[square].COL() == "white":
            [lN.append(i) for i in pMovement(square[0], square[1], board, "white")]

    for i in lN:
        print(i)

# checklegal("white")

# test()

# startGame()

def startChessEngine():

    board = createBoard()
    turnTracker = Turn()
    boardUI(board)

    
    enpSQ = None


    while True:


        legal_moves = checklegal(turnTracker.Turn(), board, "string_move", enpSQ)
        engine_moves = checklegal(turnTracker.Turn(), board, "object_move", enpSQ)
        if checkmate(legal_moves, board, turnTracker):

            if turnTracker.Turn() == "white":

                winner = "Black"

            else:

                winner = "White"

            print("Checkmate! " + winner + " wins!")

     #    move = chess_engine.engine(board, turnTracker.Turn(), engine_moves)
        parsedMoves = parseMove(move)

        if parsedMoves[0] in board and parsedMoves[1] in board and legalMove(parsedMoves, board, turnTracker) and move in checklegal(turnTracker.Turn(), board, "string_move", enpSQ):

            if enpSQ:
                if board[parsedMoves[0]].PC() == "pawn":
                    if turnTracker.Turn() == "white" and parsedMoves[1] == enpSQ.enSquare():
                        LE = parsedMoves[1][0]
                        NU = parsedMoves[1][1]
                        board[LE + str(int(NU) - 1)] = None

                    elif turnTracker.Turn() == "black" and parsedMoves[1] == enpSQ.enSquare():
                        LE = parsedMoves[1][0]
                        NU = parsedMoves[1][1]
                        board[LE + str(int(NU) + 1)] = None

            if not board[parsedMoves[0]].hasMoved():
                if board[parsedMoves[0]].PC() == "pawn":
                    enpSQ = genEnPassentSquare(parsedMoves[0], turnTracker.Turn(), parsedMoves[1], board)
            else:
                enpSQ = None

            turnTracker.moveMade(board[parsedMoves[0]], board[parsedMoves[1]])

            board[parsedMoves[0]].MOVED()
            board[parsedMoves[1]] = board[parsedMoves[0]]
            board[parsedMoves[0]] = None
            boardUI(board)

        elif move == "O-O" or move == "0-0":
            if not inCheck(turnTracker, board):
                if turnTracker.Turn() == "white":
                    if not inCheck(turnTracker, board, "f1") and not inCheck(turnTracker, board, "g1"):
                        if not board["f1"] and not board["g1"] and board["h1"].PC() == "rook" and board["h1"].COL() == turnTracker.Turn() and not board["h1"].hasMoved():

                            turnTracker.moveMade(board["e1"], "g1")

                            board["g1"] = board["e1"]
                            board["e1"] = None
                            board["f1"] = board["h1"]
                            board["h1"] = None

                            board["g1"].MOVED()
                            board["f1"].MOVED()
                            boardUI(board)
                elif turnTracker.Turn() == "black":
                    if not inCheck(turnTracker, board, "f8") and not inCheck(turnTracker, board, "g8"):
                        if not board["f8"] and not board["g8"] and board["h8"].PC() == "rook" and board["h8"].COL() == turnTracker.Turn() and not board["h8"].hasMoved():

                            turnTracker.moveMade(board["e8"], "g8")

                            board["g8"] = board["e8"]
                            board["e8"] = None
                            board["f8"] = board["h8"]
                            board["h8"] = None

                            board["g8"].MOVED()
                            board["f8"].MOVED()
                            boardUI(board)


        elif move == "O-O-O" or move == "0-0-0":

            if not inCheck(turnTracker, board):
                if turnTracker.Turn() == "white":
                    if not inCheck(turnTracker, board, "d1") and not inCheck(turnTracker, board, "c1"):
                        if not board["d1"] and not board["c1"] and board["a1"].PC() == "rook" and board["a1"].COL() == turnTracker.Turn() and not board["a1"].hasMoved():

                            turnTracker.moveMade(board["e1"], "c1")

                            board["c1"] = board["e1"]
                            board["e1"] = None
                            board["d1"] = board["a1"]
                            board["a1"] = None

                            board["c1"].MOVED()
                            board["d1"].MOVED()
                            boardUI(board)
                elif turnTracker.Turn() == "black":
                    if not inCheck(turnTracker, board, "d8") and not inCheck(turnTracker, board, "c8"):
                        if not board["d8"] and not board["c8"] and board["a8"].PC() == "rook" and board["a8"].COL() == turnTracker.Turn() and not board["a8"].hasMoved():

                            turnTracker.moveMade(board["e8"], "c8")

                            board["c8"] = board["e8"]
                            board["e8"] = None
                            board["d8"] = board["a8"]
                            board["a8"] = None

                            board["c8"].MOVED()
                            board["d8"].MOVED()
                            boardUI(board)



# startChessEngine()