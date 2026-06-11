class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l=0
        d=0
        res=[]
        for r in range(1,len(s)):
            if s[l]==s[r]:
                d=r-l+1
            else:
                if d>=3:
                    res.append([l,r-1])
                l=r
                d=0
            if r==len(s)-1 and d>=3:
                res.append([l,r])
        return res
