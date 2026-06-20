class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        prev=0
        for i in range(len(nums)):
           curr= 2*prev+nums[i]
           res.append(curr%5==0)
           prev=curr
        return res
        
