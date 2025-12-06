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
        
"""
Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
"""