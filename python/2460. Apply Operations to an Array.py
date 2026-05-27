class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        n=len(nums)
        while i+1<n:
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
            i+=1
        res=[0]*n
        i=0
        for num in nums:
            if num!=0:
                res[i]=num
                i+=1
        return res
            
