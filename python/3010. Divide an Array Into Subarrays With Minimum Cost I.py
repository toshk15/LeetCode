class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sub1=nums[0]
        nums=sorted(nums[1:])
        return sub1+nums[0]+nums[1]
