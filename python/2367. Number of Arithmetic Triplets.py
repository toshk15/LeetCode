class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s=set(nums)
        res=0
        for n in nums:
            if n + diff in s and n+2*diff in s:
                res+=1
        return res
            
