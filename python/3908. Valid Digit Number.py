class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        c = s.count(str(x))
        if c>0 and s[0]!=str(x):
            return True
        return False
