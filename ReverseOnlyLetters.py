class Solution:
    def reverseOnlyLetters(self, s: str) -> str:        
        s=list(s)
        l=0
        r=len(s)-1

        while l<r:
            if s[l].isalpha() and s[r].isalpha():
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif not s[l].isalpha():
                l+=1
            elif not s[r].isalpha():
                r-=1
        return "".join(s)
            
"""
Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""