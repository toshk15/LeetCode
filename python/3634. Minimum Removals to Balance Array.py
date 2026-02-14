class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=float("inf")
        n=len(nums)
        r=0
        for l in range(n):
            while r<n and nums[r]<=nums[l]*k:
                r+=1
            res=min(res, n-(r-l))
        return res
