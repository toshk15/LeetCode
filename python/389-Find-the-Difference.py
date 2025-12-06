from collections import Counter
def findTheDifference(s, t):
    c=Counter(s)
    cc=Counter(t)
    res=[]
    common=set(t)
    for i in common:
        r=cc.get(i,0)-c.get(i,0)
        if r==0:
            continue
        else:
            res.append(r*i)
    return "".join(res)
      
"""

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:

Input: s = "", t = "y"
Output: "y"

"""