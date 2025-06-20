def rotateArray(arr, k):
    k = k % len(arr)
    l, r = 0 , len(arr) - 1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1

    l, r = 0, k

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1
    
    l, r = k, len(arr)-1

    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1
    

    return arr

arr = [1,4,5,6,7,8,9,10]
print(rotateArray(arr, 3))

