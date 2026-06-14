class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res=0
        n=len(pref)
        
        for w in words:
            if pref in w[:n]:
                res+=1
        return res
