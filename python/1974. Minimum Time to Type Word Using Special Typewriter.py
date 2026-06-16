class Solution:
    def minTimeToType(self, word: str) -> int:
        cur="a"
        su=0
        for c in word:
            dif=abs(ord(c)-ord(cur))
            su+=min(dif, 26-dif)+1
            cur=c
        return su
