class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        i=len(s)-1
        v=set("aeiou")
        while i>=0 and s[i] in v:
            i-=1
        return s[:i+1]
