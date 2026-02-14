class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res=0
        while sum(grid[0])>0:
            maxx=float("-inf")
            for r in grid:
                m=max(r)
                maxx=max(m,maxx)
                r.remove(m)
            res+=maxx
        return res
