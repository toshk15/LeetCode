class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res=0
        s=set()
        for n in nums:
            c=0
            while n not in s:
                s.add(n)
                c+=1
                n=nums[n]
            if c>res:
                res=c
        return res
