class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            for j in range(n):
                val=(nums[i] * nums[j]) // gcd(nums[i], nums[j])**2
                res=max(res,val)
        return res
