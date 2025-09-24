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
    