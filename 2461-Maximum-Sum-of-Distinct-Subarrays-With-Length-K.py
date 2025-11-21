class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        res=0
        sumT=0
        l=0
        for r in range(len(nums)):            
            sumT+=nums[r]
            d[nums[r]]+=1

            if r-l+1>k:               
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    d.pop(nums[l])  
                sumT-=nums[l]                  
                l+=1
            if len(d)==k and r-l+1==k:
                res = max(res, sumT)
        return res
"""
 
Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.

""" 