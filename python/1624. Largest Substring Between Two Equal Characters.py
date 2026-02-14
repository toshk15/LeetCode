class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res=-1
        for ch in range(len(s)):
            a=s[ch]
            aa=[i for i in range(len(s[ch+1:])) if s[ch+1:].startswith(a,i)]
            su=aa[-1] if aa else -1
            res=max(res,su)
        return res
