def isSubsequence(s, t):
    i,j=0,0
    n = len(s)
    m=len(t)
    while i<n and j<m:
        if s[i]==t[j]:
            i+=1
            j+=1
        else:
            j+=1
    if i==n:
        return True
    else:
        return False
    

"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""