class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        cols = len(mat[0])
        rows = len(mat)
        res={}
        out=[]
        
        for i in range(rows):
            c=0
            for j in range(cols):
                if mat[i][j]==1:
                    c+=1
            res[i]=c
        sorted_res = sorted(res.items(), key=lambda item: item[1])
        sorted_res = dict(sorted_res)
        for r,s in sorted_res.items():
            out.append(r)
            k-=1
            if k==0:
                break
        return out

"""
Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].

"""