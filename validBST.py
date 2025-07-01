class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def isValidBST(root):
    def valid(node, left, right):
        if not node:
            return True
        
        if not (left < node.val < right):
            return False
        
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    
    return valid(root, float("-inf"), float("inf"))

node = Tree(5)
node.left = Tree(3)
node.right = Tree(7)
node.right.left = Tree(4)
node.right.right = Tree(8)

print(isValidBST(node))