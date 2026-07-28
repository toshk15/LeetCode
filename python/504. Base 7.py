class Solution:
    def convertToBase7(self, num: int) -> str:
        neg=num
        num=abs(num)
        s=""
        if num==0:
            return "0"
        while num:
            s+=str(num%7)
            num//=7
        s=s[::-1]
        if neg<0:
            return "-"+s
        return s
        
