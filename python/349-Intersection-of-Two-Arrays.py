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

"""
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

"""