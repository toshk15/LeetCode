class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        

def binary_tree_symetry(root):
    if not root:
        return True
    
    return dfs(root.left, root.right)

def dfs(node1, node2):
    if not node1 and not node2:
        return True
    
    if not node1 or not node2:
        return False
    
    if node1.val != node2.val:
        return False
    
    if not dfs(node1.left, node2.right):
        return False
    
    return dfs(node1.right,node2.left)

node = Tree(5)
node.left = Tree(2)
node.right = Tree(2)
node.left.left = Tree(1)
node.left.right = Tree(4)
node.left.right.left = Tree(3)

node.right.left = Tree(4)
node.right.right = Tree(1)
node.right.left.right= Tree(3)

print(binary_tree_symetry(node))



