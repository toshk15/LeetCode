def kadanes(arr):
    s = [0] * len(arr)
    s[0] = arr[0]

    for i in range(len(arr)-1):
        if s[i-1] < 0:
            s[i] = arr[i]
        else:
            s[i] = s[i-1] + arr[i]

    max = s[0]

    for i in range(len(s)-1):
        if s[i] > max:
            max = s[i]
    return max

arr = [3,-7,10,-2,-1,7,-11,-5,9,3]

print(kadanes(arr))