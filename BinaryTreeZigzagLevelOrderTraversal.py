from collections import deque
def zigzagLevelOrder(root):
    if not root:
        return []
            
    q=deque([root])
    pos=0
    res=[]
    while q:
        p=[]
        n=len(q)
        for i in range(n):                
            node = q.popleft()
            p.append(node.val)                              

            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
        if pos%2==1:
            p = p[::-1]             
        res.append(p)
        pos+=1
    return res
