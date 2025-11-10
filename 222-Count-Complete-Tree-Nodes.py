from collections import deque

def countNodes(root):
    if not root:
        return 0
    if root and not root.left and not root.right:
        return 1
    cn=0
    q=deque()
    q.append(root)

    while q:
        for i in range(len(q)):
            node=q.popleft()
            cn+=1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return cn

"""
Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1
"""