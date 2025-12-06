from collections import deque
def largestValues(root):
    if not root:
        return []

    res=[]        
    q = deque([root])

    while q:
        maxval=float("-inf")
        n=len(q)
        for i in range(n):
            node = q.popleft()
            maxval = max(maxval, node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(maxval)
    return res

"""     
Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:

Input: root = [1,2,3]
Output: [1,3]
"""   
 