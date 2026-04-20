class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        res=1
        nums.sort()
        s=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-s>k:
                res+=1
                s=nums[i]
        return res
            
