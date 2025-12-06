from collections import defaultdict
def isToeplitzMatrix(matrix):
    d = defaultdict(list)
    R=len(matrix)
    C=len(matrix[0])

    for i in range(R):
        for j in range(C):
            d[i-j].append(matrix[i][j])
       
    for o in d.values():
        o=set(o)
        if len(o)==1:
            continue
        else:
            return False
    return True

"""
sol 2 and efficient

rows = len(matrix)
        col = len(matrix[0])
        for i in range(rows - 1):
            for j in range(col - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
"""

"""
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
"""