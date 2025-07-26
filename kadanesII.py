def kadanes(arr):
    maxSub = arr[0]
    prevSum = arr[0]

    for i in range(len(arr) -1):
        if prevSum < 0:
            prevSum = arr[i]
        else:
            prevSum = prevSum + arr[i]
        
        if prevSum > maxSub:
            maxSub = prevSum
    return maxSub

arr = [3,-7,10, 2,-2]

print(kadanes(arr))