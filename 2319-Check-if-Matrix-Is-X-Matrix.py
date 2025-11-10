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


"""
Example 1:

Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
Output: true
Explanation: Refer to the diagram above. 
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is an X-Matrix.

Example 2:

Input: grid = [[5,7,0],[0,3,1],[0,5,0]]
Output: false
Explanation: Refer to the diagram above.
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is not an X-Matrix.
"""