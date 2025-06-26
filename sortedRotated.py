def sortedRotated(arr):
    n = len(arr)
    count = 1

    for i in range(1, 2*n):
        if arr[(i-1)%n] <= arr[i%n]:
            count += 1
        else:
            count = 1
        if count == n:
            return True
    return n == 1

arr = [4,5,6,1,2,3,3]
print(sortedRotated(arr))