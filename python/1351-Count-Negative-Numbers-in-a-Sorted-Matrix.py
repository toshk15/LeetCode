def countNegatives(grid):
    R=len(grid)
    C=len(grid[0])
    neg=0
    for i in range(R):
        for j in range(C):
            if grid[i][j]<0:
                neg+=1
    return neg

"""
Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
"""
        