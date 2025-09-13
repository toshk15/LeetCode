def sortColors(arr):
    l = -1
    r = len(arr)
    curr = 0

    while curr < r:
        if arr[curr] == 0:
            l += 1
            arr[l], arr[curr] = arr[curr], arr[l]
            curr+=1
        elif arr[curr] == 2:
            r-=1
            arr[r], arr[curr] = arr[curr], arr[r]
        else:
            curr+=1
    return arr

arr=[2, 0, 1, 2, 0]
print(sortColors(arr))

