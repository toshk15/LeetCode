class Solution:
    def sortString(self, s: str) -> str:
        d=Counter(s)
        d=dict(sorted(d.items(),key=lambda x:x[0]))
        res=[]
        while sum(d.values())>0:
            for i,j in d.items():
                if j>0:
                    d[i]-=1
                    res.append(i)
            for i,j in reversed(d.items()):
                if j>0:
                    d[i]-=1
                    res.append(i)
        return "".join(res)
