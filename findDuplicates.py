"""
def findDuplicates(arr):

    res = []

    for n in arr:
        n = abs(n)
        if arr[n-1] < 0:
            res.append(n)
        arr[n - 1] = -arr[n-1]
    return res

arr = [1, 2, 2, 5, 2, 6, 5, 1]
print(findDuplicates(arr))
"""

def findDuplicates(arr):
    res = []
    final = []
    for i in arr:
        if not res or i not in res:
            res.append(i)
        elif i in res and i not in final:
            final.append(i)
        
    return final
       
        


arr = [1, -2, -2, 5, 2, 6, 5, 1]
print(findDuplicates(arr))