
from collections import deque
def findSecondMinimumValue(root):
    if not root:
        return -1
        
    q = deque([root])
    res=[]
    
    while q:
        for i in range(len(q)):
            node=q.popleft()            
            if node.val not in res:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    res.sort()
    if len(res)>=2:
        return res[1]
    else:
        return -1
    

"""
Example 1:

Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:

Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""