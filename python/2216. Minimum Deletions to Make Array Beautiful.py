class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            if (i + res)%2==0:
                if i+1<n and nums[i]==nums[i+1]:
                    res+=1
        if (n-res)%2:
            res+=1
        return res

