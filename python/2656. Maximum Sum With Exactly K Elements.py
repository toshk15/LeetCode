class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s=0
        m=max(nums)
        while k>0:
           s+=m
           m+=1
           k-=1
        return s
