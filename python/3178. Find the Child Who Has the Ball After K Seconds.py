class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        one = 2*(n-1)
        pos = k%one
        if pos < n-1:
            return pos
        return one-pos
        
