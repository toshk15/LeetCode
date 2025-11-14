def shiftGrid(grid, k):
    M, N = len(grid), len(grid[0])

    def posToVal(r,c):
        return r*N+c
    
    def valToPos(v):
        return [v // N, v % N]
    
    res = [[0] * N for i in range(M)]
    for r in range(M):
        for c in range(N):
            newVal = (posToVal(r,c) + k) % (M*N)
            newR, newC = valToPos(newVal)
            res[newR][newC] = grid[r][c]

    return res

grid = [[1,2,3],[4,5,6],[7,8,9]]
print(shiftGrid(grid, 3))

"""
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows=len(grid)
        cols=len(grid[0])
        k%=cols*rows
        rotated=[[0]*cols for j in range(rows)]
        for r in range(rows):
            for c in range(cols):
                idx = r*cols+c
                new_idx=(idx+k)%(rows*cols)
                newr=new_idx//cols
                newc=new_idx%cols

                rotated[newr][newc]=grid[r][c]
        return rotated
"""


"""
Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:

Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

"""
