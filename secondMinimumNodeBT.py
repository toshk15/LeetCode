
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