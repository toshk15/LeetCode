class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            m=(l+r)//2
            c=int((m*(m+1))/2)
            if c>n:
                r=m-1
            else:
                l=m+1
                
        return r
