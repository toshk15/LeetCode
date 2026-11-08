class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res=0
        def binary(n):
            b=""
            while n:
                b=str(n%2)+b
                n//=2
            return b
        for i in range(len(nums)):
            n=binary(i)
            if n.count("1")==k:
                res+=nums[i]
        return res
                
