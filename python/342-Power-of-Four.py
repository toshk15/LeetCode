def isPowerOfFour(n):
    if n<=0:
        return False

    for i in range(0,n):
        if 4**i==n:
            return True
        if 4**i>n:
            return False
        
"""
Example 1:

Input: n = 16
Output: true

Example 2:

Input: n = 5
Output: false

Example 3:

Input: n = 1
Output: true

"""