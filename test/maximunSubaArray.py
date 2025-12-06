def maxSubArray(arr):
    res = arr[0]

    total = 0 
    for i in arr:
        total += i
        res = max(res, total)
        if total < 0:
            total = 0
    return res

arr = [3,-7,10,-2,-1,7,-11,-5,9,3]
print(maxSubArray(arr))