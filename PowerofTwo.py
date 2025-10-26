def isPowerOfTwo(self, n: int) -> bool:
    if n==1:
        return True     
    if n<=0:
        return False
    for i in range(n):
        if 2**i==n:
            return True
        if 2**i>n:
            return False
"""
Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false
"""