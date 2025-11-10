def diagonalSum(mat):
    res, n = 0, len(mat)

    for i in range(len(mat)):
        res += mat[i][i]
        res += mat[i][len(mat)-1-i]
    if n%2:
        res = res - mat[n//2][n//2]
    
    return res

#mat =[[1,2,3],[1,2,3],[1,2,3]]

mat =[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print(diagonalSum(mat))
    



"""
Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:

Input: mat = [[5]]
Output: 5
"""