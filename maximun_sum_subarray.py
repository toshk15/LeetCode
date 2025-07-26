"""
def maxsub(arr):
    max_sum = -100
    start, end = 0, 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            s = 0
            for k in range(i, j+1):
                s += arr[k]
            if s > max_sum:
                max_sum = s
                start = i
                end = j

    return max_sum, start, end
"""
"""
def maxsub(arr):
    max_sum = -100
    start, end = 0, 0
    n = len(arr) - 1
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
        if s > max_sum:
            max_sum = s
        
    return max_sum
"""

def DP(arr):
    n = len(arr)
    s = [0] * n
    s[0] = arr[0]

    for i in range(n):
        if s[i-1] < 0:
            s[i] = arr[i]
        else:
            s[i] = s[i-1] + arr[i]
    m = max(s)
    return m           

    
arr= [4,-5,8,-2,-1,7,-6]

print(DP(arr))

