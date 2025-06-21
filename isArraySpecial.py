def isArraySpecial(arr):
    for i in range(1, len(arr)):
        if arr[i] % 2 == arr[i-1] % 2:
            return False
    return True

#arr = [1,2,3]
arr = [1,2,3,5]
print(isArraySpecial(arr))