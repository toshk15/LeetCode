class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        res=1
        n=len(nums)
        score=nums[0]+nums[1]
        for i in range(2,n,2):
            if i+1<n:
               if nums[i]+nums[i+1]==score:
                   res+=1
               else:
                   break
        return res
                
