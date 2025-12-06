from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r=len(mat)
        c=len(mat[0])
        d=defaultdict(list)
        res=[]
        for i in range(r):
            for j in range(c):
                d[i+j].append(mat[i][j])

        for i,j in d.items():            
            if i%2==0:
                res+=j[::-1]
            else:
                res+=j
        return res

"""
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""