def kadanes(arr):
    n = len(arr) - 1
    start, end = 0, 0
    substart = 0
    maxsub = arr[0]
    prevsum= arr[0]

    for i in range(1, n):
        if prevsum  < 0:
            prevsum = arr[i]
            substart = i
        else:
            prevsum = prevsum + arr[i]
        
        if prevsum > maxsub:
            maxsub = prevsum
            start = substart
            end = i
    return maxsub, start, end

arr= [4,-5,8,-2,-1,7,-6]

print(kadanes(arr))