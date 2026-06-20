class Solution:
    def minimumFlips(self, n: int) -> int:
        b=bin(n)[2:]
        l=0
        r=len(b)-1
        res=0
        while l<=r:
           if b[l]!=b[r]:
              res+=2
           l+=1
           r-=1
        return res
            
