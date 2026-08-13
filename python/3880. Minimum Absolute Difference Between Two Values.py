class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        res=float("inf")
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==1 and nums[j]==2:
                    res=min(abs(i-j),res)
        if res!=float("inf"):
            return res
        else:
            return -1
                    
