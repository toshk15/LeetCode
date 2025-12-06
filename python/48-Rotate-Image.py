def rotateImage(arr):

    l, r = 0, len(arr) - 1

    while l < r:
        for i in range(r-l):

            top, bottom = l, r
            topleft = arr[top][l+i]
            arr[top][l+i] = arr[bottom-i][l]
            arr[bottom-i][l] = arr[bottom][r-i]
            arr[bottom][r-i] = arr[top+i][r]
            arr[top + i][r] = topleft

        r-=1
        l+=1
    return arr

arr = [[1,2,3], [4,5,6], [7,8,9]]
print(rotateImage(arr))


"""
def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            #print(matrix[i][j])
            #print(matrix[j][i])

        for i in range(n):
            matrix[i].reverse()
    print(matrix)

"""


"""
Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

"""