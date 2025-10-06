def sortDiagonalMatrix(mat):
    m = len(mat)
    n = len(mat[0])

    for j in range(n):
        sortF(mat, 0, j,m,n)
    for i in range(m):
        sortF(mat,i,0,m,n)

    return mat

def sortF(mat,i,j,m,n):
    values = []
    r=i
    c=j
    while r<m and c<n:
        values.append(mat[r][c])
        r+=1
        c+=1
    values.sort()

    r=i
    c=j
    idx=0
    while r<m and c<n:
        mat[r][c]=values[idx]
        idx+=1
        r+=1
        c+=1

mat = [[3,3,1],[2,2,1],[1,1,1]]
print(sortDiagonalMatrix(mat))