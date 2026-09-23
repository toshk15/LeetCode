class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            minn=float("inf")
            maxx=float("-inf")
            for j in range(i+1):
                maxx=max(nums[j],maxx)
            for jj in range(i,n):
                minn=min(nums[jj],minn)
            if maxx-minn<=k:
                return i
        return -1
