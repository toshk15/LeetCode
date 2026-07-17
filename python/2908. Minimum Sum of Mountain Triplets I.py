class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minn=float("inf")
        n=len(nums)
        for j in range(1,n-1):
            for i in range(j):
                for k in range(j+1,n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        s=nums[i]+nums[j]+nums[k]
                        minn=min(minn,s)
        if minn!=float("inf"):
            return minn
        return -1
            
