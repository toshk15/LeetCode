class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j=Counter(jewels)
        s=Counter(stones)
        t=0
        for x in j:
            if x in s:
                t+=s[x]
        return t
""" 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total=0
        for i in jewels:
            total+=stones.count(i)
        return total 
"""      
"""
Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
"""

