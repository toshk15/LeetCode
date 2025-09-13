"""
def notEqualAve(arr):
    arr.sort()
    res=[]

    l, r = 0, len(arr)-1
    while len(res) != len(arr):
        res.append(arr[l])
        l+=1

        if l<=r:
            res.append(arr[r])
            r-=1
    return res
"""
def notEqualAve(arr):
    arr.sort()
    n = len(arr)
    mid = (n+1)//2

    res = []

    for i in range(mid):
        res.append(arr[i])

        if i+mid < n:
            res.append(arr[i+mid])
    return res


arr=[5,4,3,2,1]
print(notEqualAve(arr))