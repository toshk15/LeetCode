class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=len(s)-1
        res=[]
        while i>=0:
            if s[i]=="#":
                x=chr(ord("a")+int(s[i-2:i])-1)
                res.append(x)
                i-=3
            else:
                x=chr(ord("a")+int(s[i])-1)
                res.append(x)
                i-=1
        return "".join(reversed(res))
                      
                      
        
