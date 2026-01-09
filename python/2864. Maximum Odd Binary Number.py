class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s=[i for i in s]
        l=0
        for i in range(len(s)):
            if s[i]=="1":
                s[l],s[i]=s[i],s[l]
                l+=1
        s[l-1],s[len(s)-1]=s[len(s)-1],s[l-1]
        return "".join(s)
