class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            if i%2==0:
                res+=nums[i]
            else:
                res-=nums[i]
        return res
        
