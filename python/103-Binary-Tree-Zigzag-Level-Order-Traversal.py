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

"""
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
"""
