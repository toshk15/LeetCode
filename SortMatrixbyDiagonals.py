from collections import defaultdict
def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        d=defaultdict(list)
        r=len(grid)
        c=len(grid[0])
        res=[]
        for i in range(r):
            for j in range(c):
                d[i-j].append(grid[i][j])
        print(d)

        for key in d:
            if key>=0:
                d[key].sort(reverse=True)
            else:
                d[key].sort()
        print(d)
        for i in range(r):
            for j in range(c):
                grid[i][j]=d[i-j].pop(0)
        print(grid)
        return grid

"""

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output: [[8,2,3],[9,6,7],[4,5,1]]

Example 2:

Input: grid = [[0,1],[1,2]]

Output: [[2,1],[1,0]]

"""