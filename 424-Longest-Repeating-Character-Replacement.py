class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        res=0
        l=0
        for r in range(len(s)):
            c[s[r]]= 1+c.get(s[r],0)
            while (r-l+1) - max(c.values())>k:
                c[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
    
    
"""
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""