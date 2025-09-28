"""
def intersection(arr1, arr2):
    inter = set(arr1)
    res = [] 
    for n in arr2:
        if n in inter:
            res.append(n)
            inter.remove(n)
    return res
"""
def intersection(nums1, nums2):
    n = set(nums1)
    m = set(nums2)
    res = n & m
    return list(res)
        

arr1 = [1,2,2,3,4]
arr2 = [0,2,4,5,6]

print(intersection(arr1, arr2))