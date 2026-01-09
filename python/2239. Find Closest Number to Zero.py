class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res=float("inf")
        nums.sort()
        for n in nums:
            diff=abs(0-n)
            if diff<=res:
                
                res=diff
                m=n
        return m
            
