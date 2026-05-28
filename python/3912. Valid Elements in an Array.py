class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[0]*n
        r=[]
        m=0
        for i in range(n):
            if nums[i]>m:
                res[i]=1
                m=nums[i]
        m=0
        for i in range(n-1,-1,-1):
            if nums[i]>m:
                res[i]=1
                m=nums[i]
        for i in range(len(res)):
            if res[i]!=0:
                r.append(nums[i])
        return r
        
