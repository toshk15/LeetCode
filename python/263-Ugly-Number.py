class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for x in [2,3,5]:
            while n%x==0:
                n=n//x
        return n==1
    
"""
Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.

Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

"""