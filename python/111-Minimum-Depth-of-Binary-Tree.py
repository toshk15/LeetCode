from collections import deque
def minDepth(root):
    if not root:
        return 0

    q = deque()
    q.append(root)
    depth=1

    while(q):
        for i in range(len(q)):
            node=q.popleft()

            if not node.left and not node.right:
                return depth
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth+=1
    return depth


"""
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""