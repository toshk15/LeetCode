class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        c=len(grid[0])
        r=len(grid)
        for i in range(r):
            for j in range(c):
                if j+1<c and grid[i][j]==grid[i][j+1]:
                    return False
                if i+1<r and grid[i][j]!=grid[i+1][j]:
                    return False
        return True
        
