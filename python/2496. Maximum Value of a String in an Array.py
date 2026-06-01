class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxlen=float("-inf")
        for n in strs:
            if n.isdigit():
                n=int(n)
            else:
                n=len(n)
            if n>maxlen:
                maxlen=n
        return maxlen
