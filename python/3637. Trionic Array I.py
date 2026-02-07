class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n=len(nums)
        r=1
        while r<n and nums[r-1]<nums[r]:
            r+=1
        a=r-1
        while r<n and nums[r-1]>nums[r]:
            r+=1
        b=r-1
        while r<n and nums[r-1]<nums[r]:
            r+=1
        c=r-1
        return a!=0 and a!=b and b!=c and c==n-1
