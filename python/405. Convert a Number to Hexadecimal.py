class Solution:
    def toHex(self, num: int) -> str:
        res=""
        hexa="0123456789abcdef"
        if num==0:
           return "0"
        if num<0:
           num+=2**32
        while num:
           n=num%16
           res=hexa[n]+res
           num=num//16
        return res
