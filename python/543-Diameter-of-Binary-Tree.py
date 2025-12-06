class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    res = [0]
    def diameter(root):
        if not root:
            return 0
        left = diameter(root.left)
        right = diameter(root.right)

        res[0] = max(res[0], left+right)
        return 1+max(left,right)

    diameter(root)
    return res[0]
        
root = Tree(5)
root.left = Tree(4)
root.right = Tree(6)
root.left.left = Tree(3)
root.right.right = Tree(8)

print(diameterOfBinaryTree(root))

"""
Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1
"""