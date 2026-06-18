class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)
        ex=n%k
        res=[]
        if ex:
            s=s+fill*(k-ex)
        print(s)
        for i in range(0,len(s),k):
            res.append(s[i:i+k])
        return res
    
