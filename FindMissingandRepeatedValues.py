def findMissingAndRepeatedValues(grid):
    row=len(grid)
    col=len(grid[0])
    n=row*col
    res=[]
    s=set()
    for i in range(1,n+1):
        s.add(i)
       
    for i in range(row):
        for j in range(col):
            if grid[i][j] in s:
                s.remove(grid[i][j])
            else:
                res.append(grid[i][j])
    res+=list(s)
    return res
"""
Example 1:

Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

Example 2:

Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
"""