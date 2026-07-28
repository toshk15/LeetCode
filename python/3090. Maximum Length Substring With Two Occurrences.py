class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d=defaultdict(int)
        max_len=0
        l=0
        for r in range(len(s)):
            d[s[r]]+=1
            while d[s[r]]>2:
                d[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
            
