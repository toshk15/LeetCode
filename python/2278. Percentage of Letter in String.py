class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c=Counter(s)
        n=len(s)
        if c[letter]==0:
            return 0
        return math.floor((c[letter]/n)*100)
