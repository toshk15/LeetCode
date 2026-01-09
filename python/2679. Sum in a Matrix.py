class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        s=0
        for x in nums:
            x.sort()
        nums=[[nums[j][i] for j in range(len(nums))] for i in range(len(nums[0]))]
        for x in nums:
            s+=max(x)
        return s
