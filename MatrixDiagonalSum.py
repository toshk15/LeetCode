def diagonalSum(mat):
    lon = len(mat)
    res=0

    if len(mat)==1:
        return mat[0][0]
        
    for i in range(lon):
        res+=mat[i][i]
        res+=mat[i][lon-1-i]
        
    if lon%2:
        res-=mat[lon//2][lon//2]

    return res

"""

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