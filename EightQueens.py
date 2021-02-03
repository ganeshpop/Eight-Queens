import PrintPuzzle
import SafetyCheck

def EightQueens(board,queenCount,loc,count):
    queenCount += 1
    pref = " "*(queenCount*4)
    #print(pref,"Setting Queen at ({},{})".format(loc[0],loc[1]))
    board[loc[0]][loc[1]]='Q'
    #PrintPuzzle.printPuzzle(board,pref)
    if queenCount == 8:
        count[0] = count[0] +  1
        print("Solution #{} Found".format(count[0]))
        PrintPuzzle.printPuzzle(board,pref)
        return False
    #for row in range(loc[0]+1,loc[0]+2):
    row = loc[0]+1
    for col in range(0,8):
        #print(pref,'(',row,",",col,')')
        if SafetyCheck.isSafe(row,col,board):
            board2 = CopyBoard(board)
            if EightQueens(board2,queenCount,(row,col),count):
                return True
            #else:
                #print(pref ,"Cant Place at ({},{})".format(row,col))
                #PrintPuzzle.printPuzzle(board,pref)
    # print(pref,"Failed!!")
    # PrintPuzzle.printPuzzle(board,pref)
    return False

    
    
                    
def CopyBoard(board):
    newBoard = []
    for row in board:
        line = []
        for cell in row:
            line.append(cell)
        newBoard.append(line)
    return newBoard

count = [0]
for col in range(0,8):
    board =[[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
    EightQueens(board,0,(0,col),count)

