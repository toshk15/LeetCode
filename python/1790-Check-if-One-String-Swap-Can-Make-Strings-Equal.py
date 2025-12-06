class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1)!=len(s2):
            return False
        c=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c.append(i)
            if len(c)>2:
                return False
        if len(c)==2:
            i,j = c
            if s1[i]==s2[j] and s1[j]==s2[i]:
                return True
            else:
                return False
        return len(c)==0
    
"""
Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

"""