class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def countSubs(nums, goal):
            l=0
            res=0
            currSum=0
            for r in range(len(nums)):
                currSum+=nums[r]
                while l<=r and currSum>goal:
                    currSum-=nums[l]
                    l+=1
                res+=(r-l+1)
            return res
        return (countSubs(nums,goal) - countSubs(nums,goal-1))
    
"""
Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15

"""