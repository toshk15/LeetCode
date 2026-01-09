class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c=Counter(s1.split(" ")+s2.split(" "))
        res=[]
        for i,j in c.items():
            if j==1:
                res.append(i)
        return res
