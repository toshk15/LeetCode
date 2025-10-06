from collections import deque
def levelOrder(root):
    if not root:
        return []
        
    level=[]
    q = deque([root])      
    while q: 
        res=[]           
        for i in range(len(q)):
            node = q.popleft()                
            res.append(node.val)
            #print(res)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level.append(res)
        print(level)
    return level

