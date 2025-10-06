def checkXMatrix(grid):
    cols = len(grid[0])
    rows = len(grid)


    for i in range(rows):
        for j in range(cols):
            if i == j:
                if grid[i][j] == 0:
                    return False
                continue 
            if i == cols-j-1:
                 if grid[i][j] == 0:
                    return False
                 continue             
            if grid[i][j] != 0:                
                    return False
    return True

grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]

print(checkXMatrix(grid))