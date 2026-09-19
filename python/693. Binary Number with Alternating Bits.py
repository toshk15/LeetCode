class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=""
        while n:
            b=str(n%2)+b
            n=n//2
        for i in range(1,len(b)):
            if b[i-1]==b[i]:
                return False
        return True
            
            
            
