class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)!=2:
            ns=""
            for n in range(len(s)-1):
                x=(int(s[n])+int(s[n+1]))%10
                ns+=str(x)
            s=ns
        return s[0]==s[1]
