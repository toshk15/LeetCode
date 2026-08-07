class Solution:
    def reverse(self, x: int) -> int:
        res=0
        sig=1
        if x<0:
            sig=-1
        else:
            sig=1
        x=abs(x)
        while x:
            num=x%10
            res=res*10+num
            x=x//10
        res*=sig
        if res >= 2**31 - 1 or res <= -2**31:
            return 0
        return res
