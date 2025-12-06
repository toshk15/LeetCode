class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x
        l=0
        sumT=0
        mn=-1
        for r in range(len(nums)):
            sumT+=nums[r]
            while l<=r and sumT > target:
                sumT-=nums[l]
                l+=1
            if sumT == target:
                mn=max(mn, r-l+1)
        return -1 if mn==-1 else len(nums)-mn

"""
Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
"""