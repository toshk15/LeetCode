class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows=len(mat)
        cols=len(mat[0])        
        rotatedMat = [[0]*rows for j in range(cols)]
        def findRotateMat():
            for r in range(rows):
                for c in range(cols):
                    rotatedMat[c][rows-1-r]=mat[r][c] 
            for r in range(rows):
                for c in range(cols):
                    mat[r][c]=rotatedMat[r][c]                                  
            return rotatedMat
        
        for i in range(4):
            res = findRotateMat() 
            print(res)           
            if res==target:
                return True
        return False


"""
Example 1:

Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:

Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

"""