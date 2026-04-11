class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        mindis=float("inf")
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[i]!=nums[j]:
                    continue
                for k in range(j+1,n):
                    if nums[k]==nums[j]:
                        res=abs(i - j) + abs(j - k) + abs(k - i)
                        mindis=min(mindis,res)
                        break
        return -1 if mindis==float("inf") else mindis
                    
