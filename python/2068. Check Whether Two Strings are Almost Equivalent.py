class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)
        st = set(word1) | set(word2)
        for c in st:
            if abs(a[c]-b[c])>3:
                return False
        return True
