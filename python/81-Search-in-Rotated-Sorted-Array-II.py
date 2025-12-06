class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return True

            if nums[l] < nums[m]:
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            elif nums[l]>nums[m]:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
            else:
                l+=1
        return False
    
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for ele in nums:
            if target == ele:
                return True
        return False
"""



"""
Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""