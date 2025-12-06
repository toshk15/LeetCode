class Solution:
    def maxPower(self, s: str) -> int:
        res=0
        l=0
        c=0

        for r in range(len(s)):
            cost = ord(s[r]) - ord(s[l])
            if cost==0:
                c+=1
            if cost!=0:
                while l!=r:
                    l+=1
                c=1
            res=max(c, res)                
        return res
    
"""
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ans = 1
        cur_count = 1
        cur_char = s[0]
        for char in s[1:]:
            if char == cur_char:
                cur_count += 1
            else:
                ans = max(ans, cur_count)
                cur_char = char
                cur_count = 1
        return max(ans, cur_count)
"""

"""
Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

"""