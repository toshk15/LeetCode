class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        res=0
        c=Counter(nums)
        for key,val in c.items():
            if val%k==0:
                res+=(key*val)
        return res
