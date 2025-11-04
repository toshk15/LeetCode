class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s)-1
        if len(s)==1:
            return 1
        while l<r:
            while l<len(s)-1 and s[l]==s[r]:
                l+=1
            while r>1 and l>=1 and s[l-1]==s[r]:
                if r<l:
                    return 0
                r-=1
            if s[l]!=s[r] or l==r:
                return r-l+1
        return 0

"""  
Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.

Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
"""  