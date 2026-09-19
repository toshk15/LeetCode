class Solution:
    def calculateScore(self, s: str) -> int:
        res=0
        d = defaultdict(list)
        for i,c in enumerate(s):
            ch=chr(ord("a")+ord("z")-ord(c))
            if d[ch]:
                dif=d[ch].pop()
                res+=i-dif
            else:
                d[c].append(i)
        return res
