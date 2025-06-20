def twoSum(arr, target):
   
    l, r = 0, len(arr) - 1
    arr = sorted(arr)
    res = []
    while l < r:
        s = arr[l] + arr[r]

        if target > s:
            l += 1
        elif target < s:
            r -= 1
        else:
            res.append([arr[l] , arr[r] ])
            l += 1
            r -= 1
    return res

arr = [0, 2, 3, 4, 8]
k = 7
print(twoSum(arr, k))