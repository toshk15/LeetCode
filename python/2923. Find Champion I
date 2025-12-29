class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        d=defaultdict(int)
        cols=len(grid[0])
        rows=len(grid)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    d[i]+=1
        win=max(d,key=d.get)
        return win
