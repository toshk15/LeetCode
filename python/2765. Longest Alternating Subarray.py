class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res=-1
        n=len(nums)
        for i in range(n-1):
            if nums[i+1]-nums[i]!=1:
                continue
            sig=-1
            l=2
            for j in range(i+2,n):
                if nums[j]-nums[j-1]!=sig:
                    break
                l+=1
                sig*=-1
            res=max(res,l)
        return res
                
