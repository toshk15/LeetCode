def findMaxConsecutiveOnes(nums):
    c = 0
    maxi = 0
    for i in nums:
        if i == 1:
            c+=1                           
        else:
            maxi = max(maxi, c)
            c=0

    return max(maxi, c)

"""
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

"""