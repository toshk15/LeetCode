def matrix(mat):
    row = len(mat)
    col = len(mat[0])

    res=[[float('inf') for j in range(col)] for i in range(row)]
    #print(res)

    for i in range(row):
        for j in range(col):
            if mat[i][j]==0:
                res[i][j]=0
            else:
                if i>0:
                    res[i][j]=min(res[i][j],res[i-1][j]+1)
                if j>0:
                    res[i][j]=min(res[i][j],res[i][j-1]+1)
    print(res)
    
    for i in range(row-1,-1,-1):
        for j in range(col-1,-1,-1):
            if mat[i][j]!=0:
                if i < row-1:
                    res[i][j]=min(res[i][j],res[i+1][j]+1)
                if j < col-1:
                    res[i][j]=min(res[i][j],res[i][j+1]+1)
    return res


"""


def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        queue = deque()
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = m*n
        
        directions = [(-1,0), (0,-1), (1,0), (0,1)]

        while queue:
            i, j = queue.popleft()

            for vert, hori in directions:
                if 0 <= i+vert < m and 0<= j+hori < n and mat[i+vert][j+hori] > mat[i][j]+1:
                    mat[i+vert][j+hori] = mat[i][j]+1
                    queue.append((i+vert, j+hori))
        
        return mat
        

def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # from top and left
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    left = mat[r-1][c] if r > 0 else math.inf
                    top = mat[r][c-1] if c > 0 else math.inf
                    mat[r][c] = min(left, top) + 1

        # from down and right
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] > 0:
                    right = mat[r+1][c] if r < m-1 else math.inf
                    down = mat[r][c+1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], right + 1, down + 1)

        return mat
"""


mat = [[0,0,0],[0,1,0],[1,1,1]]
print(matrix(mat))
