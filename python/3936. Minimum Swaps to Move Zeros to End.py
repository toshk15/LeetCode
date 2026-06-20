class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        l=0
        r=len(nums)-1
        res=0
        while l<r:
           if nums[l]==0 and nums[r]!=0:
              res+=1
              l+=1
              r-=1
           elif nums[r]==0:
              r-=1
           elif nums[l]!=0:
              l+=1
        return res
