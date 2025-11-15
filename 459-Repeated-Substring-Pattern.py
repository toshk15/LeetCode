class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss=s+s
        
        if s in ss[1:-1]:
            return True
        else:
            return False
"""
def repeatedSubstringPattern(s):

    s2 = s
    for i in range(int(len(s2)/2)):
        a = s[0]
        s = s[1:]+a
        if s == s2:
            return True
    return False
"""

"""
Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:

Input: s = "aba"
Output: false

Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""