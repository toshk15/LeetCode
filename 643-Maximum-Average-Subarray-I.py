class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        sumT=0
        res=float("-inf")
        maxAvg=float("-inf")

        for r in range(len(nums)):
            sumT+=nums[r]

            if r-l+1==k:
                maxAvg=sumT/k
                res=max(maxAvg,res)
                sumT-=nums[l]
                l+=1
        return res
    
"""
Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

"""