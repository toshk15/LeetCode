class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        n=[False]*51
        for i,j in ranges:
            for x in range(i,j+1):
                n[x]=True
        for i in range(left,right+1):
            if not n[i]:
                return False
        return True
            
            
