def isPowerOfThree(n):
    for i in range(n):
        if 3**i==n:
            return True
        if 3**i>n:
            return False    
    return False


"""
Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

"""