"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False      
        flag=0
        for i in range(len(s)-1):
            if flag==1:
                break
            flag=0
            for j in range(i+1, len(s)):
                ss=list(s)
                ss[i],ss[j] = ss[j],ss[i]
                ss="".join(ss)
                if ss == goal:
                    flag=1
                    break
        if flag==1:
            return True 
        else:
            return False
"""
from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False   

        sc=Counter(s)
        go=Counter(goal)

        if sc!=go:
            return False
        dif=0
        for i in range(len(s)):
            if s[i]!=goal[i]:
                dif+=1
        
        if dif==2:
            return True

        if dif==0 and any(c>1 for c in sc.values()):
            return True
        else:
            return False

"""    
Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
"""  