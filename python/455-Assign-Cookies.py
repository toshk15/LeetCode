def findContentChildren(g, s):
    g.sort()
    s.sort()
    l=r=0
    c=0
    while l<len(s):
        if l<len(s) and r<len(g) and s[l]>=g[r]:
            l+=1
            r+=1
            c+=1
        elif l==len(s):
            break
        else:
            l+=1
    return c


"""
Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
"""

