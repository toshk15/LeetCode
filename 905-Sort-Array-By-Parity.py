class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1

        while l<r:
            if nums[l]%2==0 and nums[r]%2==0:
                l+=1
            elif nums[l]%2==1 and nums[r]%2==0:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
                l+=1
            elif nums[l]%2==0 and nums[r]%2==1:
                r-=1
                l+=1
            elif nums[l]%2==1 and nums[r]%2==1:
                r-=1
        return nums
    
"""
Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:

Input: nums = [0]
Output: [0]

"""