class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid=grid
        self.n=len(grid)
        self.pos={}
        for i in range(self.n):
            for j in range(self.n):
                self.pos[self.grid[i][j]]=(i,j)

    def adjacentSum(self, value: int) -> int:
        total=0
        dir=[(0,1),(-1,0),(0,-1),(1,0)]
        i,j=self.pos[value]
        for ii,jj in dir:
            ti=i+ii
            tj=j+jj
            if 0<=ti<self.n and 0<=tj<self.n:
                total+=self.grid[ti][tj]
        return total 
            

    def diagonalSum(self, value: int) -> int:
        total=0
        dir=[[1,1],[-1,-1],[-1,1],[1,-1]]
        i,j=self.pos[value]
        for ii,jj in dir:
            ti=i+ii
            tj=j+jj
            if 0<=ti<self.n and 0<=tj<self.n:
                total+=self.grid[ti][tj]
        return total
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
