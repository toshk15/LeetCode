class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        minimum=float("inf")
        maximum=0
        for div in divisors:
            c=0
            for num in nums:
                if num%div==0:
                    c+=1
            if c>maximum:
                maximum=c
                minimum=div
            elif c==maximum:
                minimum=min(minimum,div)
        return minimum
                
