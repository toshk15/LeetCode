class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res=[]
        for b in range(1,n+1):
            a = n - b
            if "0" not in str(a) and "0" not in str(b):
                res.append(int(a))
                res.append(int(b))
                return res
        return []
    
"""

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.

Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
"""