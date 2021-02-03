
def printPuzzle(puzzle,pref):
    border = "+---+---+---+---+---+---+---+---+"
    for row in puzzle:
        print(pref,border)
        cells ="|"
        for cell in row:
            if cell == 0:
                cell = " "
            
            cells +=" {} ".format(cell)
            cells +="|"
                
        print(pref,cells )
    print(pref,border)
