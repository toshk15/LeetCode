class Solution:
    def largestEven(self, s: str) -> str:
        i=len(s)-1
        res=list(s)
        while i >= 0:
            if (ord(res[i]) - ord("0"))%2!=0:
                res.pop()
                i-=1
            else:
                return "".join(res)
        return ""
