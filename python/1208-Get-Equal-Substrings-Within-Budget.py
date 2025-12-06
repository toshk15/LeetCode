class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost=0
        l=0
        res=0
        for r in range(len(t)):
            cost+=abs(ord(s[r])-ord(t[r]))
            if cost>maxCost:
                cost-=abs(ord(s[l])-ord(t[l]))
                l+=1
            res=max(res, r-l+1)

        return res
    
"""

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.

Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.

Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.

 
"""