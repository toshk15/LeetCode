class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols=len(strs[0])
        rows=len(strs)
        flags=[True]*(rows-1)
        numDel=0

        for j in range(cols):
            f=False
            for i in range(rows-1):
                if flags[i] and strs[i][j]>strs[i+1][j]:
                    f=True
                    break
            if f:
                numDel+=1
                continue
            for i in range(rows-1):
                if strs[i][j]<strs[i+1][j]:
                    flags[i]=False
        return numDel
                    
        
