def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]: 
    R=len(matrix)   
    C=len(matrix[0])
    for i in range(R):
        for j in range(C):
            if matrix[i][j]==-1:
                m=self.findGreatest(matrix,j,R)
                matrix[i][j]=m
    return matrix

def findGreatest(self,matrix,j,R):
    m=float("-inf")
    i=0
    while i<R:
        m=max(m,matrix[i][j])
        i+=1
    return m   

"""
Input: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
Output: [[1,2,9],[4,8,6],[7,8,9]]
Explanation: The diagram above shows the elements that are changed (in blue).
- We replace the value in the cell [1][1] with the maximum value in the column 1, that is 8.
- We replace the value in the cell [0][2] with the maximum value in the column 2, that is 9.


Input: matrix = [[3,-1],[5,2]]
Output: [[3,2],[5,2]]
Explanation: The diagram above shows the elements that are changed (in blue).
"""