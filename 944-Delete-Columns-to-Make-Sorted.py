class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols=len(strs[0])
        rows=len(strs)
        m=[[0]*cols for i in range(rows)]

        for i in range(rows):
            for j in range(len(strs[i])):
                m[i][j]=strs[i][j]
        c=0        
        for j in range(cols):
            i=1
            while i<rows:
                if i<rows and m[i-1][j]<=m[i][j]:
                    i+=1
                else:
                    i+=1
                    c+=1
                    break
        return c


"""


Example 1:

Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

Example 2:

Input: strs = ["a","b"]
Output: 0
Explanation: The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.

Example 3:

Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.


"""