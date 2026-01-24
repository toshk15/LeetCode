class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        l=0
        res=[nums[l]]
        
        for r in range(1,len(nums)):
            if nums[r]-nums[r-1]==1:
                if len(nums[l:r+1])>len(res):
                    res=nums[l:r+1]
            else:
                break
                
        su=sum(res)
        while su in nums:
            su+=1
        return su
            
