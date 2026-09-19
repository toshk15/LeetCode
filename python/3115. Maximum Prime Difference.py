class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        res=0
        def prime(num):
            if num<2:
                return False
            for n in range(2,int(math.sqrt(num)+1)):
                if num%n==0:
                    return False
            return True
        for l in range(len(nums)):
            if prime(nums[l]):
                for r in range(len(nums)-1,l-1,-1):
                    if prime(nums[r]):
                        return r-l
        return res
                
        
