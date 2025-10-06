def luckyNumbers(matrix):
    t = list(zip(*matrix))
    for row in range(len(matrix)):
        m = min(matrix[row])
        ma=float("-inf")
        for col in range(len(t)):
            ma= max(t[col])
            if m==ma:
                return [m]
    return []


    """

    row_mins = {min(row) for row in matrix}      
    col_maxs = {max(col) for col in zip(*matrix)}
       
    return list(row_mins & col_maxs) 
    """
        