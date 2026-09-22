class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stk=[]
        n=len(nums)
        res=[0]*n
        for i in range(n-1,-1,-1):
            while stk and stk[-1][0]<nums[i]:
                v,idx=stk.pop()
                res[i]=max(res[i]+1,res[idx])
            stk.append([nums[i],i])
        return max(res)
        
            
