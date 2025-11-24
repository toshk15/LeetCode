class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))

        while l <= r:
            total = (l*l) + (r*r)
            if total>c:
                r-=1
            elif total<c:
                l+=1
            else:
                return True
        return False
            
"""
Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

"""