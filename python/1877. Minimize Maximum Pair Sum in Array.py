class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxsum=float("-inf")
        nums.sort()
        for n in range(len(nums)//2):
            s=nums[n]+nums[len(nums)-1-n]
            maxsum=max(maxsum,s)
        return maxsum
            
