class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<r:
            m=(l+r)//2

            if nums[m]>nums[r]:
                l=m+1          
            else:
                r=m
        mid=l

        if mid==0:
            l=0
            r=len(nums)-1
        elif target>=nums[0] and target<=nums[mid-1]:
            l=0
            r=mid-1
        else:
            l=mid
            r=len(nums)-1
        print(l)
        print(r)
        while l<=r:
            m=(l+r)//2

            if nums[m]==target:
                return m
            elif target<nums[m]:
                r=m-1
            else:
                l=m+1
        return -1

"""
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1
"""