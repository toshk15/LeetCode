class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ss=s[:k]
        ss=ss[::-1]
        s=ss+s[k:]
        return s
