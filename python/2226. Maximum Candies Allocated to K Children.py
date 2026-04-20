class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def maxCan(candies,m,k):
            cont=0
            for n in candies:
                cont+=n//m
            return cont>=k
        l=1
        r=max(candies)
        res=0
        while l<=r:
            m=(l+r)//2
            if maxCan(candies,m,k):
                res=m
                l=m+1
            else:
                r=m-1
        return res
            
            
            
            
