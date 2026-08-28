class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        c=1
        s=0
        for i in range(n-1,-1,-1):
            s+=nums[i]
            avg=s//c
            if nums[i]>avg:
                res+=1
            c+=1
        return res
