import random as r

def canPawnTakeOver(type):
    pointsB = 0
    pointsWh = 0
    if type == "WhiteRook":
        for i in range(0, 7):
            if chessBoard[i][whiteRookCol] == "BlackQueen":
                pointsB = 1 + pointsB
                pointsWh = 1 + pointsWh
        for i in range(0, 7):
            if chessBoard[whiteRookRow][i] == "BlackQueen":
                pointsB = 1 + pointsB
                pointsWh = 1 + pointsWh
    if type == "WhiteBishop":
        for i in range(whiteBishopRow, 7):
            for j in range(whiteBishopCol, 7):
                if chessBoard[i][j] == "BlackQueen":
                    pointsB = 1 + pointsB
                    pointsWh = 1 + pointsWh
        for i in range(0, whiteBishopRow):
            for j in range(0, whiteBishopCol):
                if chessBoard[i][j] == "BlackQueen":
                    pointsB = 1 + pointsB
                    pointsWh = 1 + pointsWh
    return int(pointsB), int(pointsWh)
                    

pointsBlack = 0
pointsWhite = 0

for i in range(1, 100):
    
    #calculate points each round
    pointsBlack += pointsBlack
    pointsWhite += pointsWhite

    #initialize chess board 
    chessBoard = [[" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "], 
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " ", " "],]

    #initialize pieces(in random)
    whiteRookRow = r.randint(0,7)
    whiteRookCol = r.randint(0,7)
    chessBoard[whiteRookRow][whiteRookCol] = "WhiteRook"
    
    whiteBishopRow = r.randint(0,7)
    whiteBishopCol = r.randint(0,7)
    chessBoard[whiteBishopRow][whiteBishopCol] = "WhiteBishop"

    blackQueenRow = r.randint(0,7)
    blackQueenCol = r.randint(0,7)
    chessBoard[blackQueenRow][blackQueenCol] = "BlackQueen"

    pointsBlack = canPawnTakeOver("WhiteRook") + canPawnTakeOver("WhiteBishop") + pointsBlack
    pointsWhite = canPawnTakeOver("BlackQueen") + pointsWhite


    
print("White's points after 100 games: " + str(pointsWhite))
print("Black's points after 100 games: " + str(pointsBlack))
    
     
