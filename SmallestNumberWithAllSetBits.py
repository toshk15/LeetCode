class Solution:
    def smallestNumber(self, n: int) -> int:
        res=1
        while n>res:
            res = (res<<1) | 1
        return res
    
"""
class Solution:
    def smallestNumber(self, n: int) -> int:
        a = [1,3,7,15,31,63,127,255,511,1023]
        for i in a:
            if i>=n:
        return i
        
"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        temp=1
        while temp<=n:
            temp = temp*2
        return temp-1
       



"""
Example 1:

Input: n = 5

Output: 7

Explanation:

The binary representation of 7 is "111".

Example 2:

Input: n = 10

Output: 15

Explanation:

The binary representation of 15 is "1111".

Example 3:

Input: n = 3

Output: 3
"""