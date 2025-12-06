class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        l=0
        while l < len(s):
            if not stack or stack[-1]==s[l]:
                stack.append(s[l])
                l+=1
            elif  stack and stack[-1].upper() == s[l]:
                stack.pop()
                l+=1
            elif  stack and stack[-1].lower() == s[l]:
                stack.pop()
                l+=1
            else:
                stack.append(s[l])
                l+=1
        return "".join(stack)
    
"""

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:

Input: s = "s"
Output: "s"

"""