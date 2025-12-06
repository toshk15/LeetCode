from collections import deque

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(root):
    stack = [[root, 1]]
    res = 1

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res

"""
def maxDepth(root):

    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
"""
"""
def maxDepth(root):

    if not root:
        return 0
    
    level = 0
    q = deque([root])
    while q:

        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level

"""

root = Tree(5)
root.left = Tree(4)
root.right = Tree(6)
root.left.left = Tree(3)
root.right.right = Tree(8)
root.left.left.left = Tree(1)

print(maxDepth(root))
