class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen=float("inf")
        sumT=0
        l=0
        for r in range(len(nums)):
            sumT+=nums[r]

            while sumT>=target:
                sumT-=nums[l]
                minLen=min(minLen,r-l+1)
                l+=1
        return minLen if minLen < float("inf") else 0
        
"""
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""