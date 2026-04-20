class Solution:
    def mirrorDistance(self, n: int) -> int:
        s=str(n)[::-1]
        return abs(n-int(s))
