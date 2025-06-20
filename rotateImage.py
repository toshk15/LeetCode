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
