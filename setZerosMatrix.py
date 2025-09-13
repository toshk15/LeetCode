def setZeros(matrix):

    num_rows, num_cols = len(matrix), len(matrix[0])
    rows = [False] * num_rows
    cols = [False] * num_cols

    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            if matrix[row_idx][col_idx] == 0:
                rows[row_idx] = True
                cols[col_idx] = True
    
    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            if rows[row_idx] or cols[col_idx]:
                matrix[row_idx][col_idx] = 0
    return matrix

matrix = [[1, 2, 3, 4],
          [5, 0, 7, 8],
          [9, 10, 11, 12]]

print(setZeros(matrix))