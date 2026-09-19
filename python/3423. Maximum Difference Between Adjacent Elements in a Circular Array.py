class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            j=(i+1)%n
            diff=abs(nums[i]-nums[j])
            res=max(res,diff)
        return res
