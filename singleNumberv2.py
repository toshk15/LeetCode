def singleNumber(arr):
    res=0
    for n in arr:
        res = n ^ res
    return res

arr=[2,4,2,5,4]
print(singleNumber(arr))