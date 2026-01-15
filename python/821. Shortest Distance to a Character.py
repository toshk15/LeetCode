class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        res=[(float("inf"))]*n
        prev=float("-inf")
        for curr in range(n):
            if s[curr]==c:
                prev=curr
            res[curr]=abs(curr-prev)
        prev=float("inf")
        for curr in range(n-1,-1,-1):
            if s[curr]==c:
                prev=curr
            res[curr]=min(res[curr],abs(curr-prev))
        return res
            
