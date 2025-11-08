class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]  
        comb=[]     

        def backtrack(start):
            if len(comb)==k:
                res.append(comb[:])
                return
            
            for i in range(start,n+1):
                comb.append(i)
                backtrack(i+1)
                comb.pop()
        backtrack(1)
        return res

"""
Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

"""      