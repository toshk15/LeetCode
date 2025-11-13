class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal)<len(s):
            return False
        i=0
        while i <len(s):
            ss=goal[i:]+goal[:i]
            if ss==s:
                return True
            i+=1
        return False
     

"""
Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false

"""