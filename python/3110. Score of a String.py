class Solution:
    def scoreOfString(self, s: str) -> int:
        summ=0
        for i in range(1,len(s)):
            su=abs(ord(s[i-1])-ord(s[i]))
            summ+=su
        return summ
    
