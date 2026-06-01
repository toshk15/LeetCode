class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        res=sorted(nums)
        for i in range(len(nums)):
            if res==nums:
                return i
            nums=nums[-1:]+nums[:-1]
            print(nums)
            print(res)
        return -1
