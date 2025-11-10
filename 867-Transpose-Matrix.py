def transpose(matrix):
    cols = len(matrix[0])
    rows = len(matrix)
    mat = [[0]*rows for i in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            mat[j][i] = matrix[i][j]
    return mat
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]



"""
xample 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

"""