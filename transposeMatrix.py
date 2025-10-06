def transpose(matrix):
    cols = len(matrix[0])
    rows = len(matrix)
    mat = [[0]*rows for i in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            mat[j][i] = matrix[i][j]
    return mat
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]