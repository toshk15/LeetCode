def isMonotonic(nums):
    f = [1 if nums[0]<nums[-1] else 0]
    if f[0]:
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]<=nums[j]:
                continue
            else:
                return False
    else:
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]>=nums[j]:
                continue
            else:
                return False
    return True

"""
    c1=0
    c2=0

    for i in range(len(nums)-1):
        if nums[i]<=nums[i+1]:
            c1+=1
        if nums[i]>=nums[i+1]:
            c2+=1
     
    if c1==len(nums)-1 or c2==len(nums)-1:
        return True
    else:
        return False
"""

nums = [6,5,4,4]


"""
Example 1:

Input: nums = [1,2,2,3]
Output: true

Example 2:

Input: nums = [6,5,4,4]
Output: true

Example 3:

Input: nums = [1,3,2]
Output: false
"""