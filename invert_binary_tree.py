class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def invert_binary_tree(root):
    if not root:
        return None
    
    stack = [root]
    
    while stack:
        node = stack.pop()

        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root

"""
def invert_binary_tree(root):
    if not root:
        return None
    
    root.left, root.right = root.right, root.left

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return root
"""
def preorder(root):

    if not root:
        return None
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)   

    

root = Tree(5)
root.left = Tree(4)
root.right = Tree(6)
root.left.left = Tree(3)
root.right.right = Tree(8)

node = invert_binary_tree(root)
preorder(node)