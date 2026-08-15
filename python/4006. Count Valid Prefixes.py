class Solution:
    def countValidPrefixes(self, s: str) -> int:
        z=0
        o=0
        res=0
        for i in range(len(s)):
            if s[i]=="1":
                o+=1
            else:
                z+=1
            if abs(o-z)<2:
                res+=1
        return res
        
