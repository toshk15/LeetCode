class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r = x ^ y
        c=0
        while r:
            c+=r&1
            r=r>>1
        return c
    

"""
Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:

Input: x = 3, y = 1
Output: 1
"""