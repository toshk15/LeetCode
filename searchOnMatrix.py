def searchOnMat(mat, target):

    rows, cols = len(mat), len(mat[0])

    top, bottom = 0, rows - 1

    while top <= bottom:
        row = (top + bottom) // 2

        if target > mat[row][-1]:
            top = row + 1
        elif target < mat[row][0]:
            bottom = row - 1
        else:
            break

    if not (top <= bottom):
        return False
    
    row = (top + bottom)//2
    l, r = 0, cols - 1

    while l <= r:
        m = (l+r)// 2
        if target > mat[row][m]:
            l = m + 1
        elif target < mat[row][m]:
            r = m - 1
        else:
            return True
    
    return False

mat = [[1,2,3], [4,5,6], [7,8,9]]
print(searchOnMat(mat, -1))


