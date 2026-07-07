class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        fs=sum(nums)
        ss=""
        se=0
        for n in nums:
            ss+=str(n)
        for c in ss:
            se+=int(c)
        return abs(fs-se)
