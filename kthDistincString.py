from collections import Counter
def kthDistinct(arr, k):
    c = Counter(arr)
    res=0
    for key, value in c.items():
        if value==1:
            res+=1
            if k==res:
                return key
        else:
            continue
    return ""

arr=["a","b","a"]