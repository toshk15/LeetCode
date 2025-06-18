def search2d(mat, target):
    if not mat:
        return False
    m, n = len(mat), len(mat[0])
    low = 0
    high = (m * n) - 1
    while low <= high:
        mid = (low + high)// 2
        mid_element = mat[mid//n][mid%n]

        if mid_element == target:
            return True
        elif mid_element > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

mat = [[1, 3, 5, 8],
        [10, 12, 14, 15],
        [16, 17, 18, 19],
        [21, 22, 24, 27]]

print(search2d(mat, 10))