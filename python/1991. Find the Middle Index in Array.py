class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l=0
        totalsum=sum(nums)
        for i in range(len(nums)):
            r=totalsum-l-nums[i]
            if r==l:
                return i
            l+=nums[i]
            
        return -1
            
