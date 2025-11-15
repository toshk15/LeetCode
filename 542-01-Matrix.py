class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        row=len(mat)
        col=len(mat[0])
        res=[[float('inf') for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    res[i][j]=0
                else:
                    if i>0:
                        res[i][j]=min(res[i][j], res[i-1][j]+1)
                    if j>0:
                        res[i][j]=min(res[i][j], res[i][j-1]+1)
        
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if mat[i][j]!=0:
                    if i<row-1:
                        res[i][j]=min(res[i][j], res[i+1][j]+1)
                    if j<col-1:
                        res[i][j]=min(res[i][j], res[i][j+1]+1)
        return res

"""
Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

"""