class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        ls=len(s)
        lp=len(p)
        cp=Counter(p)
        cs=Counter(s[:lp-1])
        for i in range(lp-1,ls):
            cs[s[i]]+=1
            if cs==cp:
                res.append(i-lp+1)
            last=s[i-lp+1]
            cs[last]-=1
            if cs[last]==0:
                del cs[last]
        return res
