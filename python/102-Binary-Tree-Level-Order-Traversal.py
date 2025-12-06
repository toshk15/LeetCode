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

"""
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
"""