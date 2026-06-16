class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res=[]
        s=s.split()
        for i in range(k):
            res.append(s[i])
        return " ".join(res)
            
