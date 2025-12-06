class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])

        for j in range(n):
            self.sortDia(mat,0,j,m,n)
        
        for i in range(m):
            self.sortDia(mat,i,0,m,n)

        return mat
    
    def sortDia(self,mat,i,j,m,n):
        r=i
        c=j
        res=[]
        while r<m and c<n:
            res.append(mat[r][c])
            r+=1
            c+=1
        
        res.sort()
        r=i
        c=j
        idx=0

        while r<m and c<n:
            mat[r][c]=res[idx]
            r+=1
            c+=1
            idx+=1

"""
Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Example 2:

Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
"""