def searchInsert(nums, target):
    n = len(nums)
    m = max(nums)
    mi = min(nums)

    if target>m:
        return n

    if target<mi:
        return 0

    if target in nums:
        return nums.index(target)
    else:
        for index, num in enumerate(nums):
            if num>target:
                return index
                break  
print(searchInsert([1,3,5,6], 5))

"""
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""