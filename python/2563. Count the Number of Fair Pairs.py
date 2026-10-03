class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def pairs(n):
            l=0
            r=len(nums)-1
            c=0
            while l<r:
                if nums[l]+nums[r]<n:
                    c+=r-l
                    l+=1
                else:
                    r-=1
            return c
        return pairs(upper+1)-pairs(lower)
    
                    
