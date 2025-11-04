class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                if s[l+1:r+1]==s[l+1:r+1][::-1] or s[l:r]==s[l:r][::-1]:
                    return True
                else:
                    return False
                     
            l+=1
            r-=1
            if r<=l:
                return True
        return False
    
"""
Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false
"""