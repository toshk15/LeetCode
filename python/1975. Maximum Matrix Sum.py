class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res=0
        m=float("inf")
        neg=0
        for row in matrix:
            for n in row:
                if n<0:
                    neg+=1
                m=min(abs(n),m)
                res+=abs(n)
        if neg%2:
            res-=2*m
        return res
