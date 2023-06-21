
def check(game, row, coloumn):
    
    #check in row if there is a 1
    for i in range(row):
        if game[i][coloumn]==1:
            return False
        
    #check in upper diagonal on left 
    for i , j in zip(range(row-1,-1,-1),range(coloumn-1,-1,-1)):
        if game[i][j]==1:
            return False
        
    
    #check in lower diagonal on left
    for i , j in zip(range(row-1,-1,-1),range(coloumn+1,len(game))):
        if game[i][j]==1:
            return False
    
    #if there is no 1 it is safe    
    else:
        return True
    
    
def PN_queen(game,row):
    # if I finished
    if row == len(game):
        return True
    
    for coloumn in range(len(game)):
    
        for coloumn in range(len(game)):
            # el row el 3aleh el dor
            if check(game,row,coloumn):
                game [row][coloumn] = 1
                
                print("===================================")
                print(game,"\n")
                
                if PN_queen(game, row+1):
                    return True
                
                else:
                    game [row][coloumn] = 0
                
                
    return False

    
def solve_n_queens(n):
    game = [[0]*n for _ in range(n)]
    if PN_queen(game, 0):
        for row in game:
            print(row)
    else:
        print("No solution found.")

solve_n_queens(4)
    
    
    
        
    
        
            
        

