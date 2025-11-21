class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])

        if rows*cols != r*c:
            return mat

        res=[]
        for i in range(rows):
            for j in range(cols):
                res.append(mat[i][j])

        res_final=[]
        idx=0
        for i in range(r):
            new_row=[]
            for j in range(c):
                new_row.append(res[idx])
                idx+=1
            res_final.append(new_row)

        return res_final
    

"""    

Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

"""