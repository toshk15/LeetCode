class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        cCols=0
        cRows=0
        cols=len(grid[0])
        rows=len(grid)
        for r in grid:
            for i in range(cols//2):
                if r[i]!=r[cols-i-1]:
                    cCols+=1
        for i in range(cols):
            for j in range(rows//2):
                if grid[rows-j-1][i]!=grid[j][i]:
                    cRows+=1
        return min(cRows,cCols)
            
