import PrintPuzzle 

def areDiagonalsSafe(x,y,puzzle):
    increments = [1,-1]
    for incrementX in increments:
        row = x
        col = y
        for incrementY in increments:
            row = x
            col = y
            while True:
                row = row + incrementX
                col = col + incrementY
                if not inBoard(row,col):
                    break
                if puzzle[row][col] == 'Q':
                    return False
    return True            
    
def isRowSafe(x,y,puzzle):
    for col in range(0,8):
        if puzzle[x][col] == 'Q':
            return False
    return True

def isColumnSafe(x,y,puzzle):
    for row in range(0,8):
        if puzzle[row][y] == 'Q':
            return False
    return True

def isSafe (x,y,puzzle):
    return isRowSafe(x,y,puzzle) and isColumnSafe(x,y,puzzle) and areDiagonalsSafe(x,y,puzzle)



def inBoard(x,y):
    if x >= 0 and x <= 7 and y >= 0 and y <= 7:
        return True
    else:
        return False



