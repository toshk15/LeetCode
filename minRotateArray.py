"""
def minRotateArray(nums):
    res = nums[0]
    l, r = 0, len(nums)-1

    while l < r:
        m = (l + r) // 2 

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m - 1
    return min(res, nums[l])
"""
def minRotateArray(nums):
    if nums[0] <= nums[-1]:
        return nums[0]
    
    l, r = 0, len(nums)-1

    while l<r:
        m = (l+r)//2
        
        if nums[0] <= nums[m]:
            l = m + 1
        else:
            r = m
    return nums[l]

nums = [4,5,6,-1]

print(minRotateArray(nums))