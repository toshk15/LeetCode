class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res=[]
        l=0
        r=len(s)
        for i in range(len(s)):
            if s[i]=="I":
                res.append(l)
                l+=1
            else:
                res.append(r)
                r-=1
        res.append(l)
        return res
