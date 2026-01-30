class Solution:
    def checkRecord(self, s: str) -> bool:
        t=s.count("A")
        l=0
        maxl=0
        for i in range(len(s)):
            if s[i]=="L":
                l+=1
                maxl=max(maxl,l)
            else:
                l=0
        print(maxl)
    
        if maxl>=3:
            return False
        elif t<2:
            return True
        else:
            return False
