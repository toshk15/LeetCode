"""
def minDifference(nums):
    if len(nums) <= 4:
        return 0
    
    nums.sort()
    res = float('inf')

    for l in range(4):
        r = len(nums) - 4 + l
        res = min(res, nums[r], nums[l])

    return res

"""

def minDifference(nums):
    
    n = len(nums)
    if n < 5:
        return 0

    nums.sort()
    min_difference = float('inf')
    
    for left_remove in range(4):
        right_remove = 3 - left_remove
        current_difference = nums[n - 1 - right_remove] - nums[left_remove]
        min_difference = min(min_difference, current_difference)      

    return min_difference

nums=[6,5,4,7,2,1]
print(minDifference(nums))