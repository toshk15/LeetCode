def containsNearbyDuplicate(nums, k):
    d={}       
    for i,j in enumerate(nums):
        if j in d:
            if abs(d[j]-i)<=k:
                return True
        d[j]=i
    return False

nums = [1,2,3,1]

"""
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""