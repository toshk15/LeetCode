def moveZeros(arr):
    i = j = 0

    while j < len(arr):
        if arr[j] == 0:
            j += 1
        else:
            arr[i] = arr[j]
            i+=1
            j+=1
    while i < len(arr):
        arr[i] = 0
        i+=1

    return arr

arr = [0,0,0,1,2,3]
print(moveZeros(arr))