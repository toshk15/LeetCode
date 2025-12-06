class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd=0
        res=0
        l=0
        m=l
        for r in range(len(nums)):
            if nums[r]%2:
                odd+=1
            while odd>k:
                if nums[l]%2:
                    odd-=1
                l+=1
                m=l            

            if odd==k:
                while not nums[m]%2:
                    m+=1
                res+=(m-l)+1
        return res
    
"""
Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

"""