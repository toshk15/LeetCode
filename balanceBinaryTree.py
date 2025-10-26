class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def balance_binary_tree(root):
    return balance_tree(root) != -1

def balance_tree(root):
    if not root:
        return 0
    
    node_left = balance_tree(root.left)
    node_right = balance_tree(root.right)

    if node_left == -1 and node_right == -1:
        return -1
    
    if (node_left - node_right) > 1:
        return -1
    
    return 1 + max(node_left, node_right)

"""
def isBalanced(self, root: Optional[TreeNode]) -> bool:
        b=[True]

        def height(root):
            if not root:
                return 0
            
            left=height(root.left)
            if b[0]==False:
                return 0
            right=height(root.right)

            if abs(left-right)>1:
                b[0]=False
                return 0
            return 1+max(left,right)
        height(root)
        return b[0]
"""

root = Tree(5)
root.left = Tree(4)
root.right = Tree(6)
root.left.left = Tree(3)
root.right.right = Tree(8)

print(balance_binary_tree(root))

