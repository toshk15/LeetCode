class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        res=0
        for n in nums:
            if (n&1)^1==1:
                res+=1
        return res>1
            
            
            
        
