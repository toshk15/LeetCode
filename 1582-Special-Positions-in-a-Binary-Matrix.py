class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cols=len(mat[0])
        rows=len(mat)
        c=defaultdict(int)
        r=defaultdict(int)
        res=0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==1:
                    r[i]+=1
                    c[j]+=1

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==1 and r[i]==1 and c[j]==1:
                    res+=1
        return res
    

"""

Example 1:

Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:

Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

"""