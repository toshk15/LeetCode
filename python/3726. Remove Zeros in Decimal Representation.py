class Solution:
    def removeZeros(self, n: int) -> int:
        s=str(n)
        res=[]
        for c in s:
            if c!="0":
                res.append(c)
            else:
                continue
        return int("".join(res))
