class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res=0
        for w in words:
            if w == s[:len(w)]:
                res+=1
        return res
