class Solution:
    def isPalindromic(self, s: str) -> bool:
        f=""
        def conv(n):
            b=""
            while n:
                b=str(n%2)+b
                n//=2
            return b
                
        for c in s:
            num=ord(c)
            nb=conv(num)
            dif=8-len(nb)
            if dif > 0:
                nb=dif*'0' + nb
            f+=nb
        print(f)
        l=0
        r=len(f)-1
        while l<r:
            if f[l]!=f[r]:
                return False
            l+=1
            r-=1
        return True
                
            
